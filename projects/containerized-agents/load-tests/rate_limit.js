/**
 * rate_limit.js — Burst test to validate that the rate limiter is active.
 *
 * A single VU sends 100 requests as fast as possible (no sleep between them).
 * The MessageRouter enforces a token-bucket limit of 30 messages per minute
 * per sender_id at the routing layer.  The API layer may also enforce its own
 * limits.  Either way, a burst of 100 rapid-fire requests should trigger 429
 * responses well before all 100 complete.
 *
 * Checks:
 *   1. At least some responses are 429 — confirms the limiter is working
 *   2. 429 responses contain a non-empty error body
 *   3. 200 responses contain a `message` field
 *
 * Thresholds:
 *   - The custom metric `rate_limit_429_count` must be > 0
 *   - The check "at least one 429 seen" must pass on every iteration
 *
 * NOTE: This test intentionally does NOT set a failure threshold on
 * http_req_failed because 429 is expected and counted as a "failed" HTTP
 * request by k6's default metric.
 */

import http from "k6/http";
import { check } from "k6";
import { Counter } from "k6/metrics";
import { BASE_URL, AUTH_HEADERS, AGENT_ID } from "./config.js";
import prompts from "./fixtures/prompts.json";

// ---------------------------------------------------------------------------
// Custom metrics
// ---------------------------------------------------------------------------

const count429 = new Counter("rate_limit_429_count");
const count200 = new Counter("rate_limit_200_count");

// ---------------------------------------------------------------------------
// Test configuration
// ---------------------------------------------------------------------------

const BURST_SIZE = 100;

export const options = {
  vus: 1,
  iterations: 1,
  thresholds: {
    // At least one 429 must be observed — the limiter must have fired
    rate_limit_429_count: ["count>0"],
    // Sanity: at least some requests should have succeeded before throttling
    rate_limit_200_count: ["count>0"],
  },
};

// ---------------------------------------------------------------------------
// VU logic
// ---------------------------------------------------------------------------

export default function () {
  let seen429 = false;

  for (let i = 0; i < BURST_SIZE; i++) {
    const prompt = prompts[i % prompts.length];

    const res = http.post(
      `${BASE_URL}/api/chat`,
      JSON.stringify({
        agent_id: AGENT_ID,
        message: prompt,
        stream: false,
      }),
      {
        headers: AUTH_HEADERS,
        timeout: "35s",
      }
    );

    if (res.status === 429) {
      count429.add(1);
      seen429 = true;

      // 429 must carry an error explanation in the response body
      check(res, {
        "429: response body is non-empty": (r) => r.body && r.body.length > 0,
        "429: body contains error detail": (r) => {
          try {
            const body = r.json();
            // FastAPI validation errors use { detail: "..." }
            return (
              typeof body.detail === "string" && body.detail.length > 0
            );
          } catch (_) {
            // Plain text body is also acceptable
            return r.body && r.body.length > 0;
          }
        },
      });
    } else if (res.status === 200) {
      count200.add(1);

      check(res, {
        "200: has message field": (r) => {
          try {
            return typeof r.json("message") === "string";
          } catch (_) {
            return false;
          }
        },
      });
    } else {
      // Unexpected status — log but don't hard-fail
      console.log(`[req ${i + 1}] Unexpected status: ${res.status}`);
    }
  }

  // Final assertion: the rate limiter must have kicked in at least once
  check(null, {
    "at least one 429 was returned (limiter is active)": () => seen429,
  });

  console.log(
    `Burst of ${BURST_SIZE} completed — 200s: ${count200.value}, 429s: ${count429.value}`
  );
}
