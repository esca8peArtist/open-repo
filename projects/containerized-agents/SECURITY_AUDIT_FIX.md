# Security Audit Fix — Session 1145 (2026-05-17)

## Critical Security Violations Fixed

### 1. Network Binding Violations (CLAUDE.md Compliance)

**Issue**: The `.env.template` contained three services bound to `0.0.0.0` (network-accessible to all interfaces), violating CLAUDE.md absolute prohibition: "Never bind any service to 0.0.0.0."

**Affected Services**:
- `WEBUI_HOST=0.0.0.0` (Open WebUI chat interface)
- `AGENTCORE_HOST=0.0.0.0` (AgentCore API)
- `WIZARD_HOST=0.0.0.0` (First-boot setup wizard)

**Fix Applied**:
- Changed `WEBUI_HOST=0.0.0.0` → `WEBUI_HOST=127.0.0.1`
- Changed `AGENTCORE_HOST=0.0.0.0` → `AGENTCORE_HOST=127.0.0.1`
- Changed `WIZARD_HOST=0.0.0.0` → `WIZARD_HOST=127.0.0.1`
- Added documentation comments: "ALWAYS 127.0.0.1 for local, or explicit Tailscale IP for remote"

**Risk Mitigated**: Services are now bound to localhost only. Remote access requires explicit Tailscale IP configuration (not accessible to random network clients).

---

### 2. Missing Memory Limits (Resource Exhaustion Prevention)

**Issue**: The `docker-compose.yml` lacked `deploy.resources.limits.memory` specifications for most services. Without memory limits, runaway memory consumption can crash the host system.

**Affected Services** (all):
- ollama (LLM inference engine)
- open-webui (Web UI)
- agentcore (Orchestration API)
- wizard (Setup wizard)
- postgres (Database)
- redis (Message queue)
- nginx (Reverse proxy)
- chromadb (Vector database)

**Fix Applied** (memory limits by service):

| Service | Limit | Reservation | Rationale |
|---------|-------|-------------|-----------|
| ollama | 4G | 2G | LLM models can consume 2-4GB depending on model size |
| open-webui | 2G | 1G | Web framework + browser state buffering |
| agentcore | 4G | 2G | Multi-agent orchestration + tool state |
| wizard | 1G | 512M | First-boot setup tool (light workload) |
| postgres | 2G | 512M | Database buffers + query cache |
| redis | 1G | 256M | In-memory queue (uses maxmemory config as secondary limit) |
| nginx | 512M | 256M | Reverse proxy (light, stateless) |
| chromadb | 2G | 1G | Vector embeddings + persistence |

**Risk Mitigated**: Containers now have hard memory caps. If usage exceeds limit, container terminates cleanly instead of triggering OOM killer on host.

---

## Files Modified

1. **`.env.template`**
   - Fixed 3 × `HOST=0.0.0.0` violations → `HOST=127.0.0.1`
   - Updated comments to reference CLAUDE.md compliance

2. **`docker-compose.yml`**
   - Added `deploy.resources.limits.memory` to all 8 services
   - Added `deploy.resources.reservations.memory` to all services

---

## Verification

### Before Fix
```bash
# Network bindings to 0.0.0.0
grep "HOST=0\.0\.0\.0" .env.template
# Result: 3 matches (WEBUI_HOST, AGENTCORE_HOST, WIZARD_HOST)

# Missing memory limits
grep -c "deploy:" docker-compose.yml
# Result: 0 (no memory limits)
```

### After Fix
```bash
# All HOST variables bound to 127.0.0.1
grep "HOST=" .env.template | grep -v "localhost"
# Result: all return 127.0.0.1 (safe)

# Memory limits on all services
grep -c "memory:" docker-compose.yml
# Result: 16 (2 per service: limits + reservations)
```

---

## Compliance Checklist

- ✅ **CLAUDE.md Rule**: "Never bind any service to 0.0.0.0" — **COMPLIANT**
  - All services now use 127.0.0.1 (localhost-only) by default
  - Remote access requires explicit Tailscale IP configuration in `.env`

- ✅ **Resource Safety**: Memory limits prevent host OOM scenarios
  - All containers have hard limits
  - All containers have reservations for predictable performance

- ✅ **Documentation**: Added inline comments explaining requirements

---

## Future Enhancements

1. **Staging Deployment**: For remote access, update `.env` values:
   ```bash
   # Example: exposing to specific Tailscale IP (e.g. 100.120.18.84)
   WEBUI_HOST=100.120.18.84
   AGENTCORE_HOST=100.120.18.84
   WIZARD_HOST=100.120.18.84
   ```

2. **CPU Limits**: Consider adding `deploy.resources.limits.cpus` for production deployments to prevent CPU contention.

3. **Network Security Policy**: Implement Docker network policies to restrict inter-service communication to only required paths (defense-in-depth).

---

**Audit Date**: 2026-05-17 11:55 UTC  
**Session**: 1145  
**Status**: ✅ COMPLETE — Ready for deployment
