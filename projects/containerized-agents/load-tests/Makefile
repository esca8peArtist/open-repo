# Makefile — k6 load test runner for containerized-agents
#
# Prerequisites:
#   - k6 installed (https://grafana.com/docs/k6/latest/get-started/installation/)
#   - The agentcore service running and reachable at BASE_URL
#
# Environment variables (all have defaults in config.js):
#   BASE_URL   API base URL, e.g. http://localhost:8080
#   API_KEY    X-API-Key header value
#   AGENT_ID   Agent UUID to target in chat tests (default: "default")
#
# Usage:
#   make smoke                       # quick sanity check
#   make load                        # full staged load test
#   make stress                      # push to 100 VUs
#   make soak                        # 1-hour endurance run
#   BASE_URL=http://staging.example.com make load

.PHONY: smoke load stress soak agents sessions rate-limit all

# ---------------------------------------------------------------------------
# Chat endpoint tests
# ---------------------------------------------------------------------------

## smoke: 1 VU for 30 s — confirms the server is up and responding correctly
smoke:
	k6 run --vus 1 --duration 30s chat_load.js

## load: staged ramp as defined in chat_load.js (0→10→50→0 VUs over ~5 min)
load:
	k6 run chat_load.js

## stress: push to 100 VUs to find the breaking point
stress:
	k6 run --stage 0s:0,30s:100,5m:100,30s:0 chat_load.js

## soak: sustained low load for 1 hour to detect memory leaks / degradation
soak:
	k6 run --vus 10 --duration 1h chat_load.js

# ---------------------------------------------------------------------------
# Specialised test suites
# ---------------------------------------------------------------------------

## agents: full CRUD lifecycle — 20 VUs for 90 s
agents:
	k6 run agent_crud.js

## sessions: 5 VUs each sending 10 sequential messages (conversation threading)
sessions:
	k6 run concurrent_sessions.js

## rate-limit: burst 100 requests from 1 VU to validate 429 behaviour
rate-limit:
	k6 run rate_limit.js

# ---------------------------------------------------------------------------
# Meta targets
# ---------------------------------------------------------------------------

## all: run the full suite in sequence (useful for a pre-deploy gate)
all: smoke agents sessions rate-limit load
