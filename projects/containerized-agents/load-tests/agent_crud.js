/**
 * agent_crud.js — Agent management API lifecycle test.
 *
 * Simulates 20 concurrent users each performing the full agent CRUD lifecycle:
 *   POST   /api/agents          → create
 *   GET    /api/agents/{id}     → read
 *   PUT    /api/agents/{id}     → update
 *   DELETE /api/agents/{id}     → delete
 *
 * No LLM calls are involved, so response times should be well under 500 ms.
 *
 * Thresholds:
 *   - 95th-percentile duration < 500 ms
 *   - HTTP error rate < 0.1 %
 *   - All lifecycle checks pass > 99.9 %
 */

import http from "k6/http";
import { check, group, sleep } from "k6";
import { BASE_URL, AUTH_HEADERS } from "./config.js";

// ---------------------------------------------------------------------------
// Test configuration
// ---------------------------------------------------------------------------

export const options = {
  vus: 20,
  duration: "90s",
  thresholds: {
    "http_req_duration{p(95)}": ["p(95)<500"],
    http_req_failed: ["rate<0.001"],
    checks: ["rate>0.999"],
  },
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function buildAgentPayload(suffix) {
  return JSON.stringify({
    name: `load-test-agent-${suffix}`,
    profile: "general",
    model: "llama3.1:8b",
    system_prompt: "You are a test agent created by the k6 load test suite.",
    active: true,
    channels: [],
    tools: [],
  });
}

// ---------------------------------------------------------------------------
// VU logic
// ---------------------------------------------------------------------------

export default function () {
  const suffix = `${__VU}-${Date.now()}`;
  let agentId = null;

  // ------------------------------------------------------------------
  // CREATE
  // ------------------------------------------------------------------
  group("create agent", () => {
    const res = http.post(
      `${BASE_URL}/api/agents`,
      buildAgentPayload(suffix),
      { headers: AUTH_HEADERS, timeout: "10s" }
    );

    const ok = check(res, {
      "create: status 201": (r) => r.status === 201,
      "create: returns agent_id": (r) => {
        try {
          const body = r.json();
          return typeof body.agent_id === "string" && body.agent_id.length > 0;
        } catch (_) {
          return false;
        }
      },
    });

    if (ok) {
      agentId = res.json("agent_id");
    }
  });

  if (!agentId) {
    // Cannot continue the lifecycle if create failed; bail early
    console.warn(`[VU ${__VU}] Agent creation failed — skipping remaining steps`);
    sleep(1);
    return;
  }

  // ------------------------------------------------------------------
  // READ
  // ------------------------------------------------------------------
  group("read agent", () => {
    const res = http.get(`${BASE_URL}/api/agents/${agentId}`, {
      headers: AUTH_HEADERS,
      timeout: "10s",
    });

    check(res, {
      "read: status 200": (r) => r.status === 200,
      "read: id matches": (r) => {
        try {
          return r.json("id") === agentId;
        } catch (_) {
          return false;
        }
      },
    });
  });

  // ------------------------------------------------------------------
  // UPDATE
  // ------------------------------------------------------------------
  group("update agent", () => {
    const updatedPayload = JSON.stringify({
      name: `load-test-agent-${suffix}-updated`,
      profile: "general",
      model: "llama3.1:8b",
      system_prompt: "Updated system prompt from the k6 load test suite.",
      active: true,
      channels: [],
      tools: [],
    });

    const res = http.put(
      `${BASE_URL}/api/agents/${agentId}`,
      updatedPayload,
      { headers: AUTH_HEADERS, timeout: "10s" }
    );

    check(res, {
      "update: status 200": (r) => r.status === 200,
      "update: status field is updated": (r) => {
        try {
          return r.json("status") === "updated";
        } catch (_) {
          return false;
        }
      },
    });
  });

  // ------------------------------------------------------------------
  // DELETE
  // ------------------------------------------------------------------
  group("delete agent", () => {
    const res = http.del(`${BASE_URL}/api/agents/${agentId}`, null, {
      headers: AUTH_HEADERS,
      timeout: "10s",
    });

    check(res, {
      "delete: status 200": (r) => r.status === 200,
      "delete: status field is deleted": (r) => {
        try {
          return r.json("status") === "deleted";
        } catch (_) {
          return false;
        }
      },
    });
  });

  sleep(0.5);
}
