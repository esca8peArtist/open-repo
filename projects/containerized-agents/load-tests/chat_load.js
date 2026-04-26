/**
 * chat_load.js — Primary chat endpoint load test.
 *
 * Ramp profile:
 *   0 → 10 VUs over 30 s
 *   Hold 10 VUs for 2 min
 *   10 → 50 VUs over 30 s
 *   Hold 50 VUs for 2 min
 *   50 → 0 VUs over 30 s
 *
 * Each VU POSTs to POST /api/chat with a randomly selected prompt from the
 * fixtures list and the configured API key.
 *
 * Thresholds (test fails if any are breached):
 *   - 95th-percentile response time < 30 s  (LLM completions can be slow)
 *   - HTTP error rate < 0.5 %
 *   - Custom check pass rate > 99 %
 */

import http from "k6/http";
import { check, sleep } from "k6";
import { Trend, Rate } from "k6/metrics";
import { BASE_URL, AUTH_HEADERS, AGENT_ID } from "./config.js";
import prompts from "./fixtures/prompts.json";

// ---------------------------------------------------------------------------
// Custom metrics
// ---------------------------------------------------------------------------

const chatDuration = new Trend("chat_response_duration_ms", true);
const missingMessageField = new Rate("chat_missing_message_field");

// ---------------------------------------------------------------------------
// Test configuration
// ---------------------------------------------------------------------------

export const options = {
  stages: [
    { duration: "30s", target: 10 },   // ramp up to 10 VUs
    { duration: "2m", target: 10 },    // hold at 10 VUs
    { duration: "30s", target: 50 },   // ramp up to 50 VUs
    { duration: "2m", target: 50 },    // hold at 50 VUs
    { duration: "30s", target: 0 },    // ramp down
  ],
  thresholds: {
    // 95th percentile must be under 30 s (LLM-backed endpoint)
    "http_req_duration{p(95)}": ["p(95)<30000"],
    // Less than 0.5 % of requests may fail at the HTTP transport level
    http_req_failed: ["rate<0.005"],
    // Custom check pass rate must exceed 99 %
    checks: ["rate>0.99"],
  },
};

// ---------------------------------------------------------------------------
// VU logic
// ---------------------------------------------------------------------------

export default function () {
  const prompt = prompts[Math.floor(Math.random() * prompts.length)];

  const payload = JSON.stringify({
    agent_id: AGENT_ID,
    message: prompt,
    stream: false,
  });

  const startTime = Date.now();
  const res = http.post(`${BASE_URL}/api/chat`, payload, {
    headers: AUTH_HEADERS,
    timeout: "35s",
  });
  const elapsed = Date.now() - startTime;

  chatDuration.add(elapsed);

  let body = null;
  try {
    body = res.json();
  } catch (_) {
    // non-JSON response handled by checks below
  }

  const hasMessage = body !== null && typeof body.message === "string";

  check(res, {
    "status is 200": (r) => r.status === 200,
    "response has message field": () => hasMessage,
  });

  // Track missing-message-field separately for dashboards
  missingMessageField.add(!hasMessage);

  // Log slow responses for debugging (visible in k6 output with -v)
  if (elapsed > 10000) {
    console.log(
      `[VU ${__VU}] Slow response: ${elapsed} ms | status=${res.status} | prompt="${prompt.slice(0, 60)}…"`
    );
  }

  // Brief think time between requests to avoid hammering the server
  sleep(1);
}
