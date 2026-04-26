/**
 * Shared configuration for all k6 load test scripts.
 *
 * Values are read from environment variables so that CI pipelines and local
 * runs can override them without editing scripts.
 *
 * Usage:
 *   k6 run --env BASE_URL=http://localhost:8080 --env API_KEY=secret chat_load.js
 */

export const BASE_URL = __ENV.BASE_URL || "http://localhost:8080";
export const API_KEY = __ENV.API_KEY || "dev-api-key-change-me";

/**
 * Standard headers for every authenticated request.
 * Spread these into your params.headers object:
 *
 *   http.post(url, body, { headers: { ...AUTH_HEADERS, "Content-Type": "application/json" } })
 */
export const AUTH_HEADERS = {
  "X-API-Key": API_KEY,
  "Content-Type": "application/json",
};

/**
 * Default agent_id used by chat tests.
 * Override with --env AGENT_ID=<uuid> when a specific agent is required.
 */
export const AGENT_ID = __ENV.AGENT_ID || "default";
