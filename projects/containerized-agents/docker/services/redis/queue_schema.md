# AgentCore Redis Key Schema

**Version:** 1.0
**Service:** Redis 7 (container: agentcore-redis)
**Database index:** 0 (default — all keys in db 0)

All keys are namespaced under `agentcore:` to prevent collisions if additional
applications share the Redis instance in future.

---

## Task Queues (List)

Redis Lists are used as FIFO queues. AgentCore workers use `BRPOP` (blocking
right-pop) to consume tasks. Tasks are pushed with `LPUSH` (left-push) so
the most-recently-enqueued item in the same priority bucket is processed first
within that bucket.

| Key | Type | Description |
|-----|------|-------------|
| `agentcore:queue:high` | List | High-priority tasks: voice input, real-time web queries, interactive chat |
| `agentcore:queue:normal` | List | Normal-priority tasks: Telegram messages, scheduled reminders, API requests |
| `agentcore:queue:low` | List | Low-priority tasks: batch reports, background document ingestion, analytics |

**Task envelope (JSON-serialised string stored in the List):**
```json
{
  "task_id": "uuid4",
  "agent_id": "agent-001",
  "type": "tool_call | llm_completion | pipeline_step",
  "payload": {},
  "created_at": "ISO-8601",
  "ttl_seconds": 300
}
```

---

## Agent State (Hash)

Each active agent maintains a state hash. AgentCore updates these atomically
when an agent picks up or completes a task.

| Key pattern | Type | Fields | Description |
|-------------|------|--------|-------------|
| `agentcore:agent:{agent_id}:state` | Hash | `status`, `updated_at` | Current lifecycle state of the agent |
| `agentcore:agent:{agent_id}:last_task` | Hash | `task_id`, `type`, `completed_at`, `duration_ms`, `outcome` | Metadata of the last completed task |

**`status` values:** `idle` \| `busy` \| `error` \| `offline`

---

## Inter-Agent Bus (Pub/Sub Channels)

Used by Profile 6 (Enterprise Orchestrator) for real-time coordination between
the Qwen3-72B orchestrator and Qwen2.5-7B sub-agents.

| Channel | Description |
|---------|-------------|
| `agentcore:bus:broadcast` | Fan-out: message delivered to all subscribed agents |
| `agentcore:bus:{agent_id}` | Point-to-point: direct message to a specific agent |

**Message envelope (JSON):**
```json
{
  "from": "orchestrator | agent_id",
  "type": "command | status | result | error",
  "payload": {},
  "timestamp": "ISO-8601"
}
```

---

## Cache (String with TTL)

All cache keys are Strings holding JSON-serialised payloads. TTLs are set
with `SET key value EX <seconds>`. Cache misses fall through to the upstream
source (RAG pipeline, Ollama, tool executor).

| Key pattern | Type | TTL | Description |
|-------------|------|-----|-------------|
| `agentcore:cache:rag:{query_hash}` | String | 300s | RAG retrieval results for a given query. Hash = SHA-256 of normalised query text. |
| `agentcore:cache:llm:{prompt_hash}` | String | 60s | LLM completion response cache. Hash = SHA-256 of prompt + model + generation params. |
| `agentcore:cache:tool:{tool}:{hash}` | String | varies | Tool call result cache. TTL depends on tool (e.g., web search: 120s, calendar: 30s). |

**`{query_hash}` / `{prompt_hash}` / `{hash}`:** first 16 hex characters of SHA-256
of the canonical (whitespace-normalised, lowercased) input string.

---

## Rate Limiting (String with TTL)

Sliding-window counters for per-channel rate limiting. Each key stores an
integer counter incremented with `INCR`. The key is set with `EXPIRE` on
first write; subsequent `INCR` calls within the window do not reset the TTL.

| Key pattern | Type | TTL | Description |
|-------------|------|-----|-------------|
| `agentcore:ratelimit:telegram:{chat_id}` | String | 60s | Number of requests from a Telegram chat in the current 60-second window |
| `agentcore:ratelimit:twilio:{number}` | String | 60s | Number of requests from a Twilio phone number in the current 60-second window |

**Enforcement:** AgentCore reads the counter before processing. If the value
exceeds the configured threshold (e.g., 10 messages/min for Telegram), the
request is queued to `agentcore:queue:low` or rejected with a rate-limit reply.

---

## Session (Hash with TTL: 3600s)

Active conversation sessions. Each session hash stores the serialised context
window passed to Ollama on the next turn. TTL is refreshed on every message.
Sessions expire after 1 hour of inactivity.

| Key pattern | Type | TTL | Description |
|-------------|------|-----|-------------|
| `agentcore:session:{session_id}` | Hash | 3600s | Active session context: message history, active agent, tool state, user metadata |

**Hash fields:**
| Field | Description |
|-------|-------------|
| `agent_id` | Agent handling this session |
| `user_id` | Authenticated user (Open WebUI user ID or Telegram chat ID) |
| `channel` | `webui \| telegram \| twilio_sms \| twilio_whatsapp \| voice` |
| `messages` | JSON-serialised list of `{role, content}` dicts (last N turns) |
| `created_at` | ISO-8601 timestamp of session start |
| `last_active` | ISO-8601 timestamp of last message |

---

## Key Expiry Policy

The `maxmemory-policy` is set to `allkeys-lru`. When Redis approaches the
512 MB memory limit, it evicts the least-recently-used keys across all
namespaces. Queue keys (Lists) are consumed and deleted quickly by workers,
so eviction pressure falls primarily on cache and session keys.

**Do not store critical durable state in Redis.** Conversation history and
audit logs are written to PostgreSQL. Redis holds only ephemeral/reproduced data.

---

## Operational Notes

- **Key inspection:** `redis-cli -a $REDIS_PASSWORD keys 'agentcore:*'`
- **Queue depths:** `redis-cli -a $REDIS_PASSWORD llen agentcore:queue:high`
- **Flush a specific cache namespace:** `redis-cli -a $REDIS_PASSWORD --scan --pattern 'agentcore:cache:rag:*' | xargs redis-cli -a $REDIS_PASSWORD del`
- **Monitor live commands:** `redis-cli -a $REDIS_PASSWORD monitor` (high overhead — dev only)
