# Load Tests — AgentCore k6 Suite

Performance and stress tests for the AgentCore REST API, written with [k6](https://k6.io).

---

## Prerequisites

### Install k6

**macOS (Homebrew)**

```bash
brew install k6
```

**Linux (Debian/Ubuntu)**

```bash
sudo gpg -k
sudo gpg --no-default-keyring \
  --keyring /usr/share/keyrings/k6-archive-keyring.gpg \
  --keyserver hkp://keyserver.ubuntu.com:80 \
  --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] \
  https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update && sudo apt-get install k6
```

**Windows (Chocolatey)**

```bash
choco install k6
```

**Docker**

```bash
docker pull grafana/k6
```

Full install guide: https://grafana.com/docs/k6/latest/get-started/installation/

---

## Configuration

All scripts read configuration from environment variables.  Defaults are
defined in `config.js` and work against a locally running dev server.

| Variable  | Default                      | Description                                          |
|-----------|------------------------------|------------------------------------------------------|
| `BASE_URL`| `http://localhost:8080`      | Base URL of the agentcore service                    |
| `API_KEY` | `dev-api-key-change-me`      | Value sent in the `X-API-Key` header                 |
| `AGENT_ID`| `default`                    | Agent UUID to target in chat tests                   |

Pass overrides on the command line:

```bash
k6 run --env BASE_URL=http://staging.example.com --env API_KEY=secret chat_load.js
```

---

## Running the Tests

### Quick reference (Makefile)

```bash
cd load-tests/

make smoke        # 1 VU, 30 s — sanity check
make load         # staged ramp (0 → 10 → 50 → 0 VUs, ~5 min)
make stress       # 100 VUs for 5 min — find the breaking point
make soak         # 10 VUs for 1 h — endurance / memory-leak detection
make agents       # agent CRUD lifecycle, 20 VUs, 90 s
make sessions     # 5 VUs × 10 sequential messages (conversation threading)
make rate-limit   # burst 100 requests to validate 429 behaviour
make all          # run the full suite in sequence
```

### Running individual scripts directly

```bash
# Chat load test — uses the staged ramp defined inside the script
k6 run chat_load.js

# Agent CRUD — fixed 20 VUs for 90 s
k6 run agent_crud.js

# Conversation threading — 5 VUs, 10 messages each
k6 run concurrent_sessions.js

# Rate-limiter burst test — 1 VU, 100 requests
k6 run rate_limit.js
```

---

## Script Reference

### `chat_load.js` — Chat endpoint staged load test

Simulates realistic traffic against `POST /api/chat` using 20 varied prompts
from `fixtures/prompts.json`.

**Stage profile:**

```
  VUs
  50 |        ______
  10 | ______|      |______
   0 |      30s  2m  30s  2m  30s
```

**Thresholds** (test is marked FAILED if any breach occurs):

| Metric                        | Threshold   | Rationale                                      |
|-------------------------------|-------------|------------------------------------------------|
| `http_req_duration{p(95)}`    | < 30 000 ms | LLM completions are slow; 30 s is a hard cap   |
| `http_req_failed`             | < 0.5 %     | Transport-level failures (5xx, timeouts, etc.) |
| `checks`                      | > 99 %      | status=200 AND `message` field present         |

---

### `agent_crud.js` — Agent management CRUD lifecycle

20 concurrent VUs each execute the full lifecycle:
`POST /api/agents` → `GET /api/agents/{id}` → `PUT /api/agents/{id}` → `DELETE /api/agents/{id}`.

No LLM involved, so response times should be comfortably under 500 ms.

**Thresholds:**

| Metric                        | Threshold   |
|-------------------------------|-------------|
| `http_req_duration{p(95)}`    | < 500 ms    |
| `http_req_failed`             | < 0.1 %     |
| `checks`                      | > 99.9 %    |

---

### `concurrent_sessions.js` — Conversation threading

5 VUs each send 10 sequential messages, threading them by passing the
`conversation_id` (or `session_id`) returned in the first response.

Validates session continuity: the server must maintain context across turns
within the same conversation.

**Thresholds:**

| Metric                        | Threshold   | Rationale                            |
|-------------------------------|-------------|--------------------------------------|
| `session_messages_completed`  | ≥ 50        | All 5 × 10 messages must complete    |
| `http_req_duration{p(95)}`    | < 30 000 ms | LLM-backed                           |
| `http_req_failed`             | < 0.5 %     |                                      |

---

### `rate_limit.js` — Rate limiter burst validation

1 VU sends 100 requests as fast as possible without any sleep.  The
`MessageRouter` enforces 30 messages per minute per sender; after that
threshold is exceeded, the API should return HTTP 429.

**What is checked:**

- At least one 429 was returned (the limiter is active)
- 429 responses carry a non-empty `detail` error body
- 200 responses contain the `message` field

**Thresholds:**

| Metric                  | Threshold | Rationale                         |
|-------------------------|-----------|-----------------------------------|
| `rate_limit_429_count`  | > 0       | Limiter must have fired at least once |
| `rate_limit_200_count`  | > 0       | Some requests must succeed first  |

---

## Interpreting Results

At the end of every k6 run you will see a summary like:

```
✓ checks.........................: 99.87%  ✓ 2396  ✗ 3
  data_received..................: 4.2 MB  14 kB/s
  data_sent......................: 890 kB  2.9 kB/s
  http_req_blocked...............: avg=1.2ms  min=0µs   med=5µs    max=92ms   p(90)=11µs  p(95)=17µs
  http_req_duration..............: avg=4.5s   min=312ms med=3.8s   max=29.1s  p(90)=8.2s  p(95)=12.1s
  http_req_failed................: 0.12%   ✓ 3     ✗ 2393
  iterations.....................: 2399    7.9/s
  vus............................: 50      min=1 max=50
  vus_max........................: 50      min=50 max=50
```

Key things to look for:

- **`checks` pass rate** — should stay above the configured threshold (99 %).
  A drop below indicates the server is returning incorrect or missing data.

- **`http_req_duration p(95)`** — the 95th-percentile latency.  For
  LLM-backed endpoints expect 3–20 s under low load; values approaching
  30 s mean the server is saturated.

- **`http_req_failed` rate** — k6 counts 4xx and 5xx as failures.
  Note: `rate_limit.js` intentionally generates 429s, so this rate will be
  high in that script — that is expected behaviour.

- **`iterations/s`** — effective request throughput.  Sudden drops often
  indicate a queue building up at the Ollama layer or the database.

### Exit codes

| Code | Meaning                                                 |
|------|---------------------------------------------------------|
| 0    | All thresholds passed                                   |
| 99   | One or more thresholds were breached                    |
| 108  | k6 interrupted (Ctrl-C or signal)                       |

A CI pipeline should fail the build on any non-zero exit code.

---

## Continuous Integration

Add a smoke test gate to your pipeline:

```yaml
# .github/workflows/load.yml (example)
- name: Smoke test
  run: |
    k6 run \
      --vus 1 --duration 30s \
      --env BASE_URL=${{ secrets.STAGING_URL }} \
      --env API_KEY=${{ secrets.API_KEY }} \
      load-tests/chat_load.js
```

For a full pre-deploy gate, run `make all` and check the exit code.
