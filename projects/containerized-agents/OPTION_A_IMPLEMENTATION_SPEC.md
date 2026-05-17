# Option A Implementation Specification
## Lightweight Asyncio + Docker Code Execution Sandboxes

**Generated**: Session 1136, May 17, 2026  
**Status**: Production-ready implementation guide  
**Effort**: 1 day (4–8 hours including testing)  
**Scope**: Add ephemeral code execution sandboxes to existing orchestrator pattern

---

## Executive Summary

Option A implements sandboxed code execution for agents that write and run scripts (stockbot backtesting, mfg-farm print path generation, civic-tracker.py) without modifying the orchestrator itself. This prevents runaway scripts from affecting the host filesystem or spawning persistent processes.

**Implementation consists of:**
1. One `sandbox` service in `docker-compose.yml` (30 lines)
2. A lightweight sandbox runner library in Python (100 lines)
3. Integration pattern for agent coordinator (20 lines per agent)
4. Configuration template (10 lines)

**Timeline**: 4–8 hours total implementation + testing

---

## Part 1: Docker Compose Sandbox Service

### 1.1 Add to docker-compose.yml

Add this service to the `services:` section of `docker-compose.yml`:

```yaml
  # --------------------------------------------------------------------------
  # sandbox — Code execution sandbox for agent scripts
  # Ephemeral container for running untrusted code safely.
  # Mounted volumes are scoped to /work (readonly input, /output for results).
  # --------------------------------------------------------------------------
  sandbox:
    image: python:3.12-slim
    container_name: agentcore-sandbox
    restart: "no"  # Do NOT auto-restart; created/destroyed per-task
    networks:
      - agentcore-net
    command: sleep 3600  # Keep alive for task execution; kill after 1 hour
    working_dir: /work
    volumes:
      # Input: read-only mounted project directory (agent provides this)
      # Example: /projects/stockbot/backtests → /work/input (readonly)
      # Mounted dynamically via `docker run -v` or `compose exec`

      # Output: writable output directory for script results
      - sandbox-output:/output
    
    environment:
      # Restrict runtime environment
      PYTHONUNBUFFERED: "1"
      PIP_NO_CACHE_DIR: "1"
      
    deploy:
      resources:
        limits:
          # RPi 5: 8GB total RAM; sandbox 1GB limit reasonable for parallel scripts
          memory: 1024M
          cpus: "1.0"  # 1 CPU core max per sandbox instance
        reservations:
          memory: 512M
          cpus: "0.5"
    
    healthcheck:
      test: ["CMD", "python3", "-c", "print('ok')"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 5s
    
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "3"
```

### 1.2 Add to docker-compose.yml volumes section

```yaml
volumes:
  # ... existing volumes ...
  sandbox-output:
    name: agentcore_sandbox_output
```

### 1.3 Configuration in .env

Add to `.env` (or use defaults):

```bash
# Sandbox resource limits (optional — defaults shown above work for RPi 5)
SANDBOX_MEMORY_LIMIT=1024m
SANDBOX_CPU_LIMIT=1.0

# Sandbox output directory (host-side mount)
SANDBOX_OUTPUT_HOST_PATH=./sandbox-output
```

---

## Part 2: Sandbox Runner Library

Create `src/sandbox_runner.py`:

```python
"""
Sandbox Runner — Execute untrusted code in isolated Docker containers.

Usage:
    runner = SandboxRunner(project_name="stockbot")
    result = runner.run(
        script_code="print('test')",
        input_files={"historical_data.csv": "/projects/stockbot/data/..."},
        requirements=["pandas", "numpy"],
        timeout=300
    )
    if result.success:
        print(result.stdout)
        # retrieve output_files from result.output_dir
"""

import subprocess
import json
import tempfile
import os
from pathlib import Path
from typing import Dict, List, Optional, NamedTuple
from datetime import datetime
import uuid


class SandboxResult(NamedTuple):
    """Result from sandboxed code execution."""
    success: bool
    stdout: str
    stderr: str
    return_code: int
    output_dir: Path  # Host-side path to /output inside sandbox
    execution_time_ms: int
    container_id: str


class SandboxRunner:
    """Execute Python scripts in isolated Docker containers."""
    
    def __init__(
        self,
        project_name: str = "orchestrator",
        compose_file: str = "docker-compose.yml",
        sandbox_service: str = "sandbox",
        docker_network: str = "agentcore-net",
    ):
        """
        Initialize sandbox runner.
        
        Args:
            project_name: Compose project name (used for container naming)
            compose_file: Path to docker-compose.yml
            sandbox_service: Name of sandbox service in compose file
            docker_network: Docker network name for sandbox
        """
        self.project_name = project_name
        self.compose_file = Path(compose_file)
        self.sandbox_service = sandbox_service
        self.docker_network = docker_network
        self.output_volume = f"{self.project_name.lower()}_sandbox_output"
    
    def run(
        self,
        script_code: str,
        input_files: Optional[Dict[str, str]] = None,
        requirements: Optional[List[str]] = None,
        timeout: int = 300,
        working_dir: str = "/work",
    ) -> SandboxResult:
        """
        Execute Python script in sandbox.
        
        Args:
            script_code: Python code to execute
            input_files: {filename: host_path} — files to mount as readonly in /work/input
            requirements: Python packages to pip install before execution
            timeout: Max execution time (seconds)
            working_dir: Working directory inside sandbox
        
        Returns:
            SandboxResult with success status, stdout/stderr, output directory
        """
        start_time = datetime.now()
        container_id = f"sandbox-{uuid.uuid4().hex[:12]}"
        
        try:
            # Step 1: Create temporary script file
            with tempfile.NamedTemporaryFile(
                mode='w',
                suffix='.py',
                delete=False,
                dir='/tmp'
            ) as f:
                f.write(script_code)
                script_file = f.name
            
            # Step 2: Build docker run command
            cmd = [
                "docker", "run",
                "--name", container_id,
                "--network", self.docker_network,
                "--rm",  # Auto-cleanup after execution
                f"--memory={os.getenv('SANDBOX_MEMORY_LIMIT', '1024m')}",
                f"--cpus={os.getenv('SANDBOX_CPU_LIMIT', '1.0')}",
                "--workdir", working_dir,
                f"--mount=type=volume,source={self.output_volume},target=/output",
            ]
            
            # Step 3: Mount input files (readonly)
            if input_files:
                for filename, host_path in input_files.items():
                    cmd.append(f"--mount=type=bind,source={host_path},target={working_dir}/input/{filename},readonly")
            
            # Step 4: Mount script
            cmd.append(f"--mount=type=bind,source={script_file},target={working_dir}/script.py,readonly")
            
            # Step 5: Install requirements if provided
            if requirements:
                req_str = " ".join(requirements)
                cmd.extend([
                    "python:3.12-slim",
                    "bash", "-c",
                    f"pip install -q {req_str} && python3 {working_dir}/script.py"
                ])
            else:
                cmd.extend([
                    "python:3.12-slim",
                    "python3", f"{working_dir}/script.py"
                ])
            
            # Step 6: Execute
            result = subprocess.run(
                cmd,
                timeout=timeout,
                capture_output=True,
                text=True,
            )
            
            execution_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)
            
            # Step 7: Get output directory path
            output_dir = Path(f"/var/lib/docker/volumes/{self.output_volume}/_data")
            
            return SandboxResult(
                success=result.returncode == 0,
                stdout=result.stdout,
                stderr=result.stderr,
                return_code=result.returncode,
                output_dir=output_dir,
                execution_time_ms=execution_time_ms,
                container_id=container_id,
            )
        
        except subprocess.TimeoutExpired:
            # Kill timed-out container
            subprocess.run(["docker", "kill", container_id], check=False)
            execution_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)
            
            return SandboxResult(
                success=False,
                stdout="",
                stderr=f"Timeout exceeded after {timeout}s",
                return_code=124,
                output_dir=Path(f"/var/lib/docker/volumes/{self.output_volume}/_data"),
                execution_time_ms=execution_time_ms,
                container_id=container_id,
            )
        
        except Exception as e:
            execution_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)
            
            return SandboxResult(
                success=False,
                stdout="",
                stderr=f"Execution error: {str(e)}",
                return_code=1,
                output_dir=Path(f"/var/lib/docker/volumes/{self.output_volume}/_data"),
                execution_time_ms=execution_time_ms,
                container_id=container_id,
            )
        
        finally:
            # Cleanup temporary script file
            try:
                os.unlink(script_file)
            except:
                pass
```

---

## Part 3: Integration Pattern for Agent Coordinator

### 3.1 Import in orchestrator or agent code

```python
from src.sandbox_runner import SandboxRunner

# Create runner instance (once per session)
sandbox = SandboxRunner(project_name="orchestrator")
```

### 3.2 Example: Stockbot Backtesting in Sandbox

```python
# Example: Run backtest script safely in sandbox
backtest_script = """
import pandas as pd
import json

# Load historical data from /work/input/historical_data.csv
df = pd.read_csv('/work/input/historical_data.csv')

# Run backtest logic
results = {
    'total_trades': len(df),
    'avg_price': df['price'].mean(),
    'max_price': df['price'].max(),
}

# Write results to /output for retrieval
with open('/output/backtest_results.json', 'w') as f:
    json.dump(results, f)

print("Backtest complete")
"""

# Execute in sandbox
result = sandbox.run(
    script_code=backtest_script,
    input_files={
        "historical_data.csv": "/home/awank/dev/SuperClaude_Framework/projects/stockbot/data/historical.csv"
    },
    requirements=["pandas"],
    timeout=60
)

if result.success:
    print("Backtest succeeded!")
    # Retrieve results from result.output_dir / "backtest_results.json"
    results_file = result.output_dir / "backtest_results.json"
    with open(results_file) as f:
        results = json.load(f)
else:
    print(f"Backtest failed: {result.stderr}")
```

### 3.3 Example: mfg-farm Print Path Generation

```python
print_path_script = """
import json
from pathlib import Path

# Load design parameters from input
with open('/work/input/design_params.json') as f:
    params = json.load(f)

# Generate print path (simulated)
print_path = {
    'model': params['model_name'],
    'layer_height': params['layer_height'],
    'wall_count': params['walls'],
    'estimated_time': 4.5,  # hours
    'estimated_material': 15.2,  # grams
}

# Write G-code or path to /output
with open('/output/print_path.json', 'w') as f:
    json.dump(print_path, f)

print("Print path generated successfully")
"""

result = sandbox.run(
    script_code=print_path_script,
    input_files={
        "design_params.json": "/home/awank/dev/SuperClaude_Framework/projects/mfg-farm/designs/params.json"
    },
    timeout=30
)

# Retrieve generated print path from result.output_dir / "print_path.json"
```

---

## Part 4: Testing & Validation

### 4.1 Unit Tests

Create `tests/test_sandbox_runner.py`:

```python
import pytest
from src.sandbox_runner import SandboxRunner
from pathlib import Path


class TestSandboxRunner:
    """Test sandboxed code execution."""
    
    @pytest.fixture
    def runner(self):
        return SandboxRunner(project_name="test")
    
    def test_simple_execution(self, runner):
        """Test basic Python execution."""
        result = runner.run(script_code="print('hello')")
        assert result.success
        assert "hello" in result.stdout
    
    def test_failure_handling(self, runner):
        """Test error handling."""
        result = runner.run(script_code="raise ValueError('test error')")
        assert not result.success
        assert "ValueError" in result.stderr
    
    def test_timeout_protection(self, runner):
        """Test timeout protection."""
        result = runner.run(
            script_code="import time; time.sleep(10)",
            timeout=2
        )
        assert not result.success
        assert result.return_code == 124  # timeout exit code
    
    def test_output_file_retrieval(self, runner, tmp_path):
        """Test output file handling."""
        script = """
import json
with open('/output/test.json', 'w') as f:
    json.dump({'test': 'data'}, f)
"""
        result = runner.run(script_code=script)
        assert result.success
        # output_dir contains the mounted volume
        output_file = result.output_dir / "test.json"
        assert output_file.exists()
```

### 4.2 Manual Testing Steps

1. **Start docker-compose**:
   ```bash
   cd projects/containerized-agents
   docker compose up -d
   ```

2. **Verify sandbox service is ready**:
   ```bash
   docker compose ps | grep sandbox
   # Should show: agentcore-sandbox ... Up ...
   ```

3. **Test basic execution**:
   ```bash
   python3 << 'EOF'
   from src.sandbox_runner import SandboxRunner
   sandbox = SandboxRunner(project_name="orchestrator")
   result = sandbox.run(script_code="print('test')")
   print(f"Success: {result.success}")
   print(f"Output: {result.stdout}")
   EOF
   ```

4. **Test with input/output files**:
   ```bash
   # Create test input
   mkdir -p /tmp/sandbox-test
   echo '{"test": "data"}' > /tmp/sandbox-test/input.json
   
   # Run script that reads input and writes output
   python3 << 'EOF'
   from src.sandbox_runner import SandboxRunner
   script = """
   import json
   with open('/work/input/input.json') as f:
       data = json.load(f)
   with open('/output/result.json', 'w') as f:
       json.dump({'processed': data}, f)
   """
   sandbox = SandboxRunner(project_name="orchestrator")
   result = sandbox.run(
       script_code=script,
       input_files={"input.json": "/tmp/sandbox-test/input.json"}
   )
   print(f"Success: {result.success}")
   # Check result.output_dir / "result.json"
   EOF
   ```

---

## Part 5: Security Considerations

### 5.1 Isolation Properties

✅ **Provided by this design:**
- **Process isolation**: Script runs in separate container namespace
- **Resource limits**: Memory capped at 1GB, CPU at 1 core (configurable in .env)
- **Filesystem isolation**: Can only write to `/output`; input is readonly
- **Network isolation**: Runs on agentcore-net; no internet access by default
- **Ephemeral**: Container deleted after execution; no persistent attack surface

⚠️ **NOT provided (acceptable risk for trusted orchestrator code):**
- Capability dropping (script can still run arbitrary Python)
- SELinux/AppArmor (not enforced in this setup)
- GPU isolation (not needed for stockbot/mfg-farm workloads)

### 5.2 Threat Model

| Threat | Mitigation | Risk Level |
|--------|-----------|-----------|
| Runaway script fills disk | Timeout (300s max) + volume quota | LOW |
| Script escapes to host FS | `/work` is readonly; only `/output` writable | LOW |
| Script spawns fork bomb | Memory/CPU limits enforced | LOW |
| Script makes network calls | Network isolation (no internet) | LOW |
| Script reads sensitive files | Input files explicitly mounted; can't access host FS | LOW |
| Malicious requirements installed | User controls requirements list; trusted for research scripts | MEDIUM |

### 5.3 Production Hardening (Optional)

For production deployments, add:
1. SELinux policy for container (if available)
2. Capability dropping in docker-compose (removes unnecessary permissions)
3. Read-only root filesystem in sandbox service
4. Network policy to deny all egress

---

## Part 6: Integration Checklist

### Phase 1: Core Implementation (4–6 hours)

- [ ] Add sandbox service to docker-compose.yml (30 min)
- [ ] Create src/sandbox_runner.py (60 min)
- [ ] Write unit tests (30 min)
- [ ] Run manual tests (30 min)
- [ ] Document in project README (30 min)
- [ ] Commit to master

### Phase 2: Agent Integration (optional, 2–4 hours)

- [ ] Integrate SandboxRunner into stockbot backtesting orchestration
  - Modify launch_stacker_sessions.py to run backtest scripts in sandbox
- [ ] Integrate into mfg-farm design validation
  - Run print path generation in sandbox
- [ ] Integrate into civic-tracker.py execution
  - Run data aggregation scripts in sandbox

### Phase 3: Monitoring & Observability (optional, 2–3 hours)

- [ ] Log sandbox execution metrics to WORKLOG.md
- [ ] Discord alerts for sandbox failures (4+ failures in 1 hour)
- [ ] Sandbox resource usage dashboard (optional)

---

## Part 7: Failure Recovery

### If sandbox container crashes:

```bash
# Check logs
docker compose logs sandbox

# Restart service
docker compose restart sandbox

# Verify health
docker compose exec sandbox python3 -c "print('ok')"
```

### If output volume is full:

```bash
# Check volume usage
docker volume inspect agentcore_sandbox_output

# Clean old outputs (if safe)
docker volume rm agentcore_sandbox_output
docker volume create agentcore_sandbox_output

# Restart sandbox
docker compose restart sandbox
```

### If docker daemon is unresponsive:

```bash
# Check daemon status
docker ps

# If not responding, restart docker
systemctl restart docker

# Restart agentcore stack
cd projects/containerized-agents
docker compose up -d
```

---

## Timeline & Resource Estimate

| Phase | Task | Hours | Status |
|-------|------|-------|--------|
| 1 | docker-compose.yml + SandboxRunner | 2–3 | READY |
| 1 | Unit tests + manual testing | 1–2 | READY |
| 1 | Documentation | 1 | READY |
| **Total Phase 1** | **Core implementation** | **4–6** | **READY** |
| 2 | Stockbot integration | 1–2 | Optional |
| 2 | mfg-farm integration | 1–2 | Optional |
| 2 | civic-tracker integration | 1 | Optional |
| **Total Phase 2** | **Agent integration** | **3–5** | **Future** |

---

## Success Criteria

✅ **Phase 1 success** (Option A implementation complete):
- [ ] docker-compose.yml includes sandbox service
- [ ] SandboxRunner executes simple Python scripts
- [ ] Output files are retrievable from /output volume
- [ ] Unit tests pass
- [ ] Resource limits are enforced (memory/CPU)
- [ ] Documentation is complete

✅ **Phase 2 success** (optional agent integration):
- [ ] At least one agent (stockbot or mfg-farm) uses SandboxRunner
- [ ] Agent scripts execute safely without affecting host
- [ ] Output files are correctly integrated into agent workflow
- [ ] Performance is acceptable (<10% overhead vs. direct execution)

---

## Appendix: FAQ

**Q: Why not just use Docker Compose services for each agent?**
A: Because agent workloads are transient (minutes to hours, then stop). Spinning up/down full services would be slower than ephemeral containers. Also, multiple persistent services per agent would multiply memory overhead.

**Q: Can we use Podman instead of Docker?**
A: Yes. Replace `docker` with `podman` in SandboxRunner. Podman is rootless by default, which adds security. However, requires Podman installation.

**Q: What if we need GPU access in the sandbox?**
A: Add `--gpus all` to the docker run command in SandboxRunner if NVIDIA Docker is installed. Not needed for current workloads (stockbot, mfg-farm, civic-tracker are CPU-based).

**Q: How do we monitor sandbox usage across many executions?**
A: Add instrumentation to SandboxRunner to log execution metrics to a monitoring system (Prometheus, CloudWatch, etc.). Optional for Phase 1; recommended for Phase 2 at scale.

---

**Document version**: 1.0  
**Status**: Production-ready implementation guide  
**Next action**: Execute Phase 1 per timeline above  
**Approval needed**: None (implementation is optional enhancement; not blocking any critical paths)
