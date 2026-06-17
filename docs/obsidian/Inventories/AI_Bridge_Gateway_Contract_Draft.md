# AI Bridge Gateway Contract Draft

Status: draft classification generated from readonly inspection.

## Source

Repository:

    D:\dev\autocode\ai-bridge

Git status:

    ## main...origin/main
    ?? docs/EXTENSION_MESSAGE_TYPES_2026-06-08.md
    ?? scripts/watcher/diag_extension_api_events.mjs
    ?? scripts/watcher/diag_gateway_queue_notice_20260608.ps1
    ?? scripts/watcher/diag_payload_and_empty_next_action.mjs
    ?? scripts/watcher/diag_railway_all.ps1
    ?? scripts/watcher/diag_railway_bridge_db_state.mjs
    ?? scripts/watcher/diag_railway_bridge_deep.ps1
    ?? scripts/watcher/diag_stop_point_api_db.mjs
    ?? scripts/watcher/diag_stop_point_extension.ps1
    ?? scripts/watcher/diag_target_command_events_strict.mjs
    ?? scripts/watcher/inspect_ack_flow_0121_20260609.ps1
    ?? scripts/watcher/inspect_auto_recover_stale_interchat_20260609.ps1
    ?? scripts/watcher/inspect_extension_delivery_sweep_20260608.ps1
    ?? scripts/watcher/inspect_extension_next_action_flow_20260609.ps1
    ?? scripts/watcher/inspect_interchat_delivery_0120_failure_20260609.ps1
    ?? scripts/watcher/inspect_next_action_contract.ps1
    ?? scripts/watcher/inspect_post_event_endpoint_20260609.ps1
    ?? scripts/watcher/patch_next_action_contract_and_extension_guard.cjs
    ?? scripts/watcher/patch_next_action_contract_and_extension_guard_v2.cjs
    ?? scripts/watcher/smoke_interchat_roundtrip_0120_20260609.ps1
    ?? scripts/watcher/smoke_interchat_roundtrip_0121_20260609.ps1
    ?? scripts/watcher/smoke_interchat_roundtrip_0122_20260609.ps1

HEAD:

    c852816 (HEAD -> main, origin/main, origin/HEAD) Fix empty next-action contract and extension guard

## Purpose

Classify the ai-bridge gateway/API files that WS AI Office should study before any integration.

This document does not approve command execution.

## Current architecture correction

WS AI Office should use the local gateway flow from:

    D:\dev\autocode\ai-bridge

It should not use ai-bridge-local as its implementation base.

## Candidate files inspected

- apps/watcher-api/src/server.mjs
- apps/watcher-api/src/broker.mjs
- apps/watcher-api/src/message-queue.mjs
- apps/watcher-api/src/health-check.mjs
- apps/watcher-api/src/passive-ingest.mjs
- apps/watcher-api/src/db-query.mjs
- apps/watcher-api/src/file-ops.mjs
- apps/watcher-api/src/git-op.mjs
- apps/watcher-api/package.json
- apps/watcher-api/railway.toml
- apps/watcher-api/README.md
- apps/watcher-api/scripts/smoke-bridge-railway.mjs
- apps/watcher-api/scripts/smoke-bridge.mjs
- apps/watcher-api/scripts/smoke-health.mjs
- extension-next/background.js
- extension-next/capability_router.js
- extension-next/content_script.js
- extension-next/manifest.json
- docs/RAILWAY_DATABASE_AND_GATEWAY_NOTES_2026-05-30.md
- docs/RAILWAY_GATEWAY_NEXT_STATUS_2026-05-30.md
- docs/EXTENSION_API_AND_GATEWAY_PRIORITY_PLAN_2026-06-01.md
- docs/WATCHER_RECOVERY_STATUS_2026-06-08.md
- docs/API_CENTRALIZED_EXECUTION_TELEMETRY_2026-06-04.md

## Missing candidate files


## Preliminary file roles

### apps/watcher-api

Likely Railway/API service area. It contains server, broker, queue, health, passive ingest and operational scripts.

### extension-next

Likely browser extension side. It may be responsible for message delivery, event posting, ACK confirmation and next-action handling.

### docs

Likely operational source of truth for gateway, Railway database, extension/API priority and recovery status.

## Route/API evidence

- apps/watcher-api/src/health-check.mjs:3: const response = await fetch(url);
- apps/watcher-api/src/file-ops.mjs:34: const res = await fetch(apiUrl, { headers });
- apps/watcher-api/src/file-ops.mjs:57: const res = await fetch(apiUrl, { headers });
- apps/watcher-api/src/file-ops.mjs:90: const existingRes = await fetch(apiUrl, { headers });
- apps/watcher-api/src/file-ops.mjs:107: const putRes = await fetch(apiUrl, {
- apps/watcher-api/src/git-op.mjs:37: const res = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/commits?sha=${ref}&per_page=5`, { headers });
- apps/watcher-api/src/git-op.mjs:53: const res = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/commits?per_page=${count}`, { headers });
- apps/watcher-api/src/git-op.mjs:60: const res = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/branches`, { headers });
- apps/watcher-api/src/git-op.mjs:68: const res = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/commits?per_page=${count}`, { headers });
- apps/watcher-api/src/git-op.mjs:84: const res = await fetch(`${GITHUB_API_BASE}/repos/${GITHUB_REPO}/compare/${base}...${head}`, { headers });
- apps/watcher-api/scripts/smoke-bridge.mjs:9: const response = await fetch(`${baseUrl}${path}`, {
- apps/watcher-api/scripts/smoke-health.mjs:41: const response = await fetch(url);
- apps/watcher-api/scripts/smoke-health.mjs:75: await fetch(localHealthUrl);
- extension-next/background.js:202: await fetch(`${GATEWAY_BASE}/bridge/events`, {
- extension-next/background.js:257: const response = await fetch(`${base}${path}`, {
- extension-next/background.js:795: const response = await fetch(`${GATEWAY_BASE}/health`, {
- extension-next/background.js:1930: const response = await fetch("https://watcher-api-production-56ad.up.railway.app/bridge/message-observations", {
- extension-next/capability_router.js:46: const res = await fetch(gatewayBase + "/health", { signal: controller.signal });
- extension-next/capability_router.js:81: const res = await fetch(RAILWAY_API_BASE + endpoint, {
- extension-next/content_script.js:143: const res = await fetch(DEFAULT_CLOUD_API_BASE + "/bridge/visibility-resume", {
- extension-next/content_script.js:538: const response = await fetch(eventEndpoint, {
- extension-next/content_script.js:1093: const res = await fetch(url, {
- extension-next/content_script.js:1182: const response = await fetch(`${RAILWAY_BRAIN_INGEST_BASE}/api/brain/ingest`, {
- extension-next/content_script.js:1292: await fetch(`${passiveApiBase}/bridge/message-observations`, {

## Environment/config evidence

- apps/watcher-api/src/server.mjs:1: import http from "node:http";
- apps/watcher-api/src/server.mjs:2: import { createHash } from "node:crypto"; import { Pool } from "pg"; import { handleGitOp } from "./git-op.mjs"; import { handleCodexAnalyze } from "./codex-analyze.mjs"; import { handleDbQuery, setDbQueryPool } from "./db-query.mjs"; import { enqueueMessage, 
- apps/watcher-api/src/server.mjs:4: const PORT = Number(process.env.PORT ?? 8785);
- apps/watcher-api/src/server.mjs:9: const databaseUrl = process.env.DATABASE_URL;
- apps/watcher-api/src/server.mjs:11: // GIT_OP_CLOUD_ACTION_V2 - imported from ./git-op.mjs
- apps/watcher-api/src/server.mjs:15: if (process.env.PGSSLMODE === "disable") return false;
- apps/watcher-api/src/server.mjs:16: if (process.env.PGSSLMODE === "require") return { rejectUnauthorized: false };
- apps/watcher-api/src/server.mjs:24: // Railway private/internal Postgres endpoints do not use public TLS.
- apps/watcher-api/src/server.mjs:25: if (url.hostname.endsWith(".railway.internal") || url.hostname === "postgres.railway.internal") {
- apps/watcher-api/src/server.mjs:36: process.env.PGHOST &&
- apps/watcher-api/src/server.mjs:37: process.env.PGPORT &&
- apps/watcher-api/src/server.mjs:38: process.env.PGDATABASE &&
- apps/watcher-api/src/server.mjs:39: process.env.PGUSER &&
- apps/watcher-api/src/server.mjs:40: process.env.PGPASSWORD
- apps/watcher-api/src/server.mjs:54: host: process.env.PGHOST,
- apps/watcher-api/src/server.mjs:55: port: Number(process.env.PGPORT || 5432),
- apps/watcher-api/src/server.mjs:56: database: process.env.PGDATABASE,
- apps/watcher-api/src/server.mjs:57: user: process.env.PGUSER,
- apps/watcher-api/src/server.mjs:58: password: process.env.PGPASSWORD,
- apps/watcher-api/src/server.mjs:59: ssl: process.env.PGSSLMODE === "require" ? { rejectUnauthorized: false } : false
- apps/watcher-api/src/server.mjs:83: const value = process.env[name] || "";
- apps/watcher-api/src/server.mjs:94: PGHOST: sanitizeEnvValueShape("PGHOST"),
- apps/watcher-api/src/server.mjs:95: PGPORT: sanitizeEnvValueShape("PGPORT"),
- apps/watcher-api/src/server.mjs:105: database_url_present: Boolean(databaseUrl),
- apps/watcher-api/src/server.mjs:107: env_pgsslmode: process.env.PGSSLMODE || null,
- apps/watcher-api/src/server.mjs:108: db_host: null,
- apps/watcher-api/src/server.mjs:109: db_port: null,
- apps/watcher-api/src/server.mjs:114: // DB_DEBUG_PORT_NAME_V1
- apps/watcher-api/src/server.mjs:119: payload.db_host = process.env.PGHOST || null;
- apps/watcher-api/src/server.mjs:120: payload.db_port = process.env.PGPORT || null;
- apps/watcher-api/src/server.mjs:121: payload.db_name = process.env.PGDATABASE || null;
- apps/watcher-api/src/server.mjs:123: payload.effective_ssl = process.env.PGSSLMODE === "require" ? "enabled" : "disabled";
- apps/watcher-api/src/server.mjs:131: payload.db_host = url.hostname || null;
- apps/watcher-api/src/server.mjs:132: payload.db_port = url.port || null;
- apps/watcher-api/src/server.mjs:136: payload.db_host = "parse_failed";
- apps/watcher-api/src/server.mjs:158: host: process.env.PGHOST,
- apps/watcher-api/src/server.mjs:159: port: Number(process.env.PGPORT || 5432),
- apps/watcher-api/src/server.mjs:160: database: process.env.PGDATABASE,
- apps/watcher-api/src/server.mjs:161: user: process.env.PGUSER,
- apps/watcher-api/src/server.mjs:162: password: process.env.PGPASSWORD,
- apps/watcher-api/src/server.mjs:241: if (databaseUrl && process.env.DB_PROBE_INCLUDE_DATABASE_URL === "1") {
- apps/watcher-api/src/server.mjs:250: probeCases.push(["database_url_derived_ssl", {
- apps/watcher-api/src/server.mjs:256: probeCases.push(["database_url_ssl_disabled", {
- apps/watcher-api/src/server.mjs:262: probeCases.push(["database_url_ssl_enabled_reject_unauthorized_false", {
- apps/watcher-api/src/server.mjs:274: database_url_present: Boolean(databaseUrl),
- apps/watcher-api/src/server.mjs:276: env_pgsslmode: process.env.PGSSLMODE || null,
- apps/watcher-api/src/server.mjs:277: db_host: process.env.PGHOST || null,
- apps/watcher-api/src/server.mjs:278: db_port: process.env.PGPORT || null,
- apps/watcher-api/src/server.mjs:279: db_name: process.env.PGDATABASE || null,
- apps/watcher-api/src/server.mjs:280: database_url_cases_enabled: process.env.DB_PROBE_INCLUDE_DATABASE_URL === "1",
- apps/watcher-api/src/server.mjs:287: if (!pool) return { ok: false, reason: "database_url_missing" };
- apps/watcher-api/src/server.mjs:312: // CLOUD_BRIDGE_V1
- apps/watcher-api/src/server.mjs:313: const MAX_JSON_BODY_BYTES = Number(process.env.MAX_JSON_BODY_BYTES ?? 256000);
- apps/watcher-api/src/server.mjs:363: async function ensureBridgeSchema() {
- apps/watcher-api/src/server.mjs:394: throw new Error("database_url_missing");
- apps/watcher-api/src/server.mjs:443: create table if not exists bridge_commands (
- apps/watcher-api/src/server.mjs:463: create index if not exists bridge_commands_target_status_created_idx
- apps/watcher-api/src/server.mjs:464: on bridge_commands (target_chat_id, status, created_at)
- apps/watcher-api/src/server.mjs:469: alter table bridge_commands add column if not exists claimed_at timestamptz,
- apps/watcher-api/src/server.mjs:483: create table if not exists bridge_command_events (
- apps/watcher-api/src/broker.mjs:7: export function setBrokerPool(pool) {
- apps/watcher-api/src/broker.mjs:37: export async function ingestMessage(body) {
- apps/watcher-api/src/broker.mjs:130: export async function smartClaim(targetChatId, instanceId, options = {}) {
- apps/watcher-api/src/broker.mjs:213: export async function updateMessageStatus(messageId, status, errorText = null) {
- apps/watcher-api/src/broker.mjs:255: export async function getQueueStats(targetChatId = null) {
- apps/watcher-api/src/broker.mjs:288: if (body.reply_to_command_id) return 2; // Replies are important
- apps/watcher-api/src/message-queue.mjs:6: export function setQueuePool(pool) {
- apps/watcher-api/src/message-queue.mjs:11: export async function enqueueMessage(body) {
- apps/watcher-api/src/message-queue.mjs:56: export async function claimNextMessage(targetChatId, instanceId) {
- apps/watcher-api/src/message-queue.mjs:124: export async function ackMessage(messageId, status = "delivered") {
- apps/watcher-api/src/message-queue.mjs:144: export async function getQueueStats(targetChatId) {
- apps/watcher-api/src/message-queue.mjs:163: export async function runCleanup() {
- apps/watcher-api/src/health-check.mjs:1: const url = process.env.WATCHER_API_HEALTH_URL ?? "http://127.0.0.1:8785/health";
- apps/watcher-api/src/passive-ingest.mjs:53: function parseBridgeJson(raw) {
- apps/watcher-api/src/passive-ingest.mjs:93: export async function ensurePassiveIngestSchema(pool) {
- apps/watcher-api/src/passive-ingest.mjs:95: create table if not exists bridge_message_observations (
- apps/watcher-api/src/passive-ingest.mjs:114: await pool.query(`drop index if exists bridge_message_observations_message_id_uidx`);
- apps/watcher-api/src/passive-ingest.mjs:117: create unique index if not exists bridge_message_observations_message_id_uidx
- apps/watcher-api/src/passive-ingest.mjs:118: on bridge_message_observations (message_id)
- apps/watcher-api/src/passive-ingest.mjs:122: create index if not exists bridge_message_observations_chat_created_idx
- apps/watcher-api/src/passive-ingest.mjs:123: on bridge_message_observations (chat_id, created_at)
- apps/watcher-api/src/passive-ingest.mjs:127: create table if not exists bridge_command_candidates (
- apps/watcher-api/src/passive-ingest.mjs:129: observation_id bigint references bridge_message_observations(id) on delete set null,
- apps/watcher-api/src/passive-ingest.mjs:152: create unique index if not exists bridge_command_candidates_hash_uidx
- apps/watcher-api/src/passive-ingest.mjs:153: on bridge_command_candidates (candidate_hash)
- apps/watcher-api/src/passive-ingest.mjs:157: create index if not exists bridge_command_candidates_status_idx
- apps/watcher-api/src/passive-ingest.mjs:158: on bridge_command_candidates (validation_status, parse_status, created_at)
- apps/watcher-api/src/passive-ingest.mjs:162: create index if not exists bridge_command_candidates_chat_created_idx
- apps/watcher-api/src/passive-ingest.mjs:163: on bridge_command_candidates (chat_id, created_at)
- apps/watcher-api/src/passive-ingest.mjs:165: await pool.query(`alter table bridge_command_candidates add column if not exists feedback_sent_at timestamptz`);
- apps/watcher-api/src/passive-ingest.mjs:166: await pool.query(`alter table bridge_command_candidates add column if not exists feedback_command_id text`);
- apps/watcher-api/src/passive-ingest.mjs:169: export function extractCommandCandidateBlocks(body) {
- apps/watcher-api/src/passive-ingest.mjs:184: const startName = "BRIDGE_ASSISTANT_COMMAND_START";
- apps/watcher-api/src/passive-ingest.mjs:185: const endName = "BRIDGE_ASSISTANT_COMMAND_END";
- apps/watcher-api/src/passive-ingest.mjs:187: { start: lt + lt + lt + startName + gt + gt + gt, end: lt + lt + lt + endName + gt + gt + gt, type: "complete_bridge_command" },
- apps/watcher-api/src/passive-ingest.mjs:188: { start: startName, end: endName, type: "complete_bridge_command_unwrapped" }
- apps/watcher-api/src/passive-ingest.mjs:243: return "oversized_inline_command:payload.command is too large for reliable chat transport; use a script file or artifact/upload flow";
- apps/watcher-api/src/passive-ingest.mjs:272: function classifyRawCommandTransportRisk(rawText = "") {
- apps/watcher-api/src/passive-ingest.mjs:341: export function analyzeCommandCandidate(rawBlock, markerType, isFinal) {
- apps/watcher-api/src/passive-ingest.mjs:346: const transportRisk = pending ? "" : classifyRawCommandTransportRisk(rawBlock);
- apps/watcher-api/src/passive-ingest.mjs:348: parse_status: pending ? "streaming_incomplete" : (transportRisk ? "truncated_inline_command" : markerType),
- apps/watcher-api/src/passive-ingest.mjs:350: validation_errors: pending ? [] : [transportRisk || markerType],
- apps/watcher-api/src/passive-ingest.mjs:359: const parseResult = parseBridgeJson(rawBlock);
- apps/watcher-api/src/passive-ingest.mjs:362: const transportRisk = isFinal === false ? "" : classifyRawCommandTransportRisk(rawBlock);
- apps/watcher-api/src/passive-ingest.mjs:364: parse_status: transportRisk ? "truncated_inline_command" : "malformed_json",
- apps/watcher-api/src/passive-ingest.mjs:366: validation_errors: [transportRisk || ("malformed_json:" + cleanText(error?.message || error, 180))],
- apps/watcher-api/src/passive-ingest.mjs:388: errors.push("unsupported_action:" + action);
- apps/watcher-api/src/passive-ingest.mjs:441: insert into bridge_command_candidates (
- apps/watcher-api/src/passive-ingest.mjs:482: export async function ingestMessageObservation(pool, canonicalChatId, body) {
- apps/watcher-api/src/passive-ingest.mjs:497: insert into bridge_message_observations (
- apps/watcher-api/src/passive-ingest.mjs:506: observed_at = coalesce(excluded.observed_at, bridge_message_observations.observed_at),
- apps/watcher-api/src/passive-ingest.mjs:545: export async function ingestCommandCandidate(pool, canonicalChatId, body) {
- apps/watcher-api/src/passive-ingest.mjs:557: export async function getIngestStatus(pool, chatId = null) {
- apps/watcher-api/src/passive-ingest.mjs:565: `select count(*)::int as count from bridge_message_observations ${where}`,
- apps/watcher-api/src/passive-ingest.mjs:571: from bridge_command_candidates ${where}
- apps/watcher-api/src/passive-ingest.mjs:580: from bridge_command_candidates ${where}
- apps/watcher-api/src/passive-ingest.mjs:592: from bridge_message_observations ${where}
- apps/watcher-api/src/passive-ingest.mjs:618: "Use um unico bloco BRIDGE_ASSISTANT_COMMAND com JSON puro.",
- apps/watcher-api/src/passive-ingest.mjs:625: suggestions.unshift("O comando inline/base64 grande demais foi recebido pela API, mas nao foi executado por risco de truncamento no transporte do chat.");
- apps/watcher-api/src/passive-ingest.mjs:634: "AI Bridge API: comando recebido, mas nao executado.",
- apps/watcher-api/src/passive-ingest.mjs:648: export function shouldSuppressRejectedCandidateFeedback(row) {
- apps/watcher-api/src/passive-ingest.mjs:671: // MALFORMED_JSON_COMPLETE_COMMAND_FEEDBACK_20260609: a complete bridge command with malformed JSON is actionable.
- apps/watcher-api/src/passive-ingest.mjs:675: markerType === "complete_bridge_command" &&
- apps/watcher-api/src/passive-ingest.mjs:677: !haystack.includes("AI Bridge API: comando recebido") &&
- apps/watcher-api/src/passive-ingest.mjs:678: !haystack.includes("[bridge] comando recebido pela API")
- apps/watcher-api/src/passive-ingest.mjs:701: const isFullPlaceholderExample = haystack.includes("BRIDGE_ASSISTANT_COMMAND_START") && haystack.includes("BRIDGE_ASSISTANT_COMMAND_END") && haystack.includes("...");
- apps/watcher-api/src/passive-ingest.mjs:712: "AI Bridge API: comando recebido",
- apps/watcher-api/src/passive-ingest.mjs:736: if (markerType === "complete_bridge_command_unwrapped") {
- apps/watcher-api/src/passive-ingest.mjs:737: suggestions.push("Reenvie usando os delimitadores canonicos <<<BRIDGE_ASSISTANT_COMMAND_START>>> e <<<BRIDGE_ASSISTANT_COMMAND_END>>>. Use novo command_id.");
- apps/watcher-api/src/passive-ingest.mjs:739: suggestions.push("Use JSON puro entre BRIDGE_ASSISTANT_COMMAND_START e BRIDGE_ASSISTANT_COMMAND_END.");
- apps/watcher-api/src/passive-ingest.mjs:753: "[bridge] comando recebido pela API, mas nao executado.",
- apps/watcher-api/src/passive-ingest.mjs:766: export async function sendRejectedCandidateFeedback(pool, observationId, insertBridgeCommand) {
- apps/watcher-api/src/passive-ingest.mjs:769: if (process.env.BRIDGE_INGEST_REJECTION_FEEDBACK === "false") {
- apps/watcher-api/src/db-query.mjs:1: // DB_QUERY_CLOUD_ACTION_V1 - SQL queries via Railway PostgreSQL
- apps/watcher-api/src/db-query.mjs:6: export function setDbQueryPool(pool) {
- apps/watcher-api/src/db-query.mjs:10: export async function handleDbQuery(body) {
- apps/watcher-api/src/file-ops.mjs:5: const GITHUB_REPO = "HelpUSA/ai-bridge";
- apps/watcher-api/src/file-ops.mjs:10: "User-Agent": "ai-bridge-watcher-api"
- apps/watcher-api/src/file-ops.mjs:12: const token = process.env.GITHUB_TOKEN || "";
- apps/watcher-api/src/file-ops.mjs:19: export async function handleFileOps(body) {
- apps/watcher-api/src/file-ops.mjs:128: return { error: "unsupported_file_op: " + action };
- apps/watcher-api/src/git-op.mjs:4: const GITHUB_REPO = "HelpUSA/ai-bridge";
- apps/watcher-api/src/git-op.mjs:10: "User-Agent": "ai-bridge-watcher-api"
- apps/watcher-api/src/git-op.mjs:12: const token = process.env.GITHUB_TOKEN || "";
- apps/watcher-api/src/git-op.mjs:19: export async function handleGitOp(body) {
- apps/watcher-api/src/git-op.mjs:27: throw new Error(`git_op_unsupported: ${operation}. Allowed: ${allowedOps.join(", ")}`);
- apps/watcher-api/package.json:18: "smoke:bridge": "node scripts/smoke-bridge.mjs",
- apps/watcher-api/package.json:19: "smoke:bridge:remote": "node scripts/smoke-bridge.mjs",
- apps/watcher-api/package.json:21: "smoke:bridge:railway": "node scripts/smoke-bridge-railway.mjs"
- apps/watcher-api/railway.toml:1: # Railway service configuration for the watcher-api service.
- apps/watcher-api/railway.toml:2: # The production service must expose DATABASE_URL in its environment.
- apps/watcher-api/README.md:3: Cloud-first AI Bridge watcher gateway skeleton.
- apps/watcher-api/README.md:9: - `GET /health` - returns service health and validates a database connection using `DATABASE_URL`.
- apps/watcher-api/README.md:14: DATABASE_URL=postgres://...
- apps/watcher-api/README.md:15: PORT=8785
- apps/watcher-api/README.md:18: `DATABASE_URL` belongs only on the server/Railway environment. Do not place it in the Chrome extension, frontend, browser bundle, or client-side code.
- apps/watcher-api/README.md:28: ## Railway
- apps/watcher-api/README.md:30: Configure a Railway service from this directory with:
- apps/watcher-api/README.md:37: Railway must provide `DATABASE_URL` from the Production Postgres service.
- apps/watcher-api/README.md:52: - `smoke:health:no-db` starts the API without `DATABASE_URL` and expects a safe 503 response.

## Gateway flow evidence

- apps/watcher-api/src/server.mjs:2: import { createHash } from "node:crypto"; import { Pool } from "pg"; import { handleGitOp } from "./git-op.mjs"; import { handleCodexAnalyze } from "./codex-analyze.mjs"; import { handleDbQuery, setDbQueryPool } from "./db-query.mjs"; import { enqueueMessage, 
- apps/watcher-api/src/server.mjs:5: const SERVICE_NAME = "watcher-api";
- apps/watcher-api/src/server.mjs:6: const API_DEPLOY_MARKER = "rejection-feedback-delivery-adbcc74";
- apps/watcher-api/src/server.mjs:76: setQueuePool(pool);
- apps/watcher-api/src/server.mjs:171: function timeoutResult(name, startedAt, timeoutMs) {
- apps/watcher-api/src/server.mjs:193: const result = await probePool.query("select 1::int as ok");
- apps/watcher-api/src/server.mjs:198: row_ok: result.rows?.[0]?.ok === 1
- apps/watcher-api/src/server.mjs:211: timer = setTimeout(() => resolve(timeoutResult(name, startedAt, timeoutMs)), timeoutMs);
- apps/watcher-api/src/server.mjs:292: const result = await client.query("select now() as now, current_database() as database");
- apps/watcher-api/src/server.mjs:293: return { ok: true, ...result.rows[0] };
- apps/watcher-api/src/server.mjs:443: create table if not exists bridge_commands (
- apps/watcher-api/src/server.mjs:445: command_id text not null unique,
- apps/watcher-api/src/server.mjs:453: status text not null default 'queued',
- apps/watcher-api/src/server.mjs:457: acked_at timestamptz,
- apps/watcher-api/src/server.mjs:463: create index if not exists bridge_commands_target_status_created_idx
- apps/watcher-api/src/server.mjs:464: on bridge_commands (target_chat_id, status, created_at)
- apps/watcher-api/src/server.mjs:469: alter table bridge_commands add column if not exists claimed_at timestamptz,
- apps/watcher-api/src/server.mjs:471: add column if not exists heartbeat_at timestamptz,
- apps/watcher-api/src/server.mjs:483: create table if not exists bridge_command_events (
- apps/watcher-api/src/server.mjs:485: command_id text not null,
- apps/watcher-api/src/server.mjs:486: event_type text not null,
- apps/watcher-api/src/server.mjs:499: create table if not exists bridge_events (
- apps/watcher-api/src/server.mjs:510: create index if not exists bridge_events_chat_created_idx
- apps/watcher-api/src/server.mjs:511: on bridge_events (chat_id, created_at)
- apps/watcher-api/src/server.mjs:514: // PENDING_REPLIES_VIEW_V1
- apps/watcher-api/src/server.mjs:516: CREATE OR REPLACE VIEW pending_replies AS
- apps/watcher-api/src/server.mjs:517: SELECT parent.command_id AS original_command_id,
- apps/watcher-api/src/server.mjs:526: FROM bridge_commands parent
- apps/watcher-api/src/server.mjs:530: AND parent.status IN ('queued','retry','processing','delivered')
- apps/watcher-api/src/server.mjs:532: SELECT 1 FROM bridge_commands reply
- apps/watcher-api/src/server.mjs:533: WHERE (reply.payload_json->>'reply_to_command_id') = parent.command_id
- apps/watcher-api/src/server.mjs:538: // PENDING_REPLIES_VIEW_V1
- apps/watcher-api/src/server.mjs:565: event_id bigint references bridge_events(id) on delete set null,
- apps/watcher-api/src/server.mjs:573: command_id text,
- apps/watcher-api/src/server.mjs:580: create unique index if not exists app_chat_messages_event_id_uidx
- apps/watcher-api/src/server.mjs:581: on app.chat_messages (event_id)
- apps/watcher-api/src/server.mjs:582: where event_id is not null
- apps/watcher-api/src/server.mjs:595: function normalizeBridgeCommandForInsert(command) {
- apps/watcher-api/src/server.mjs:596: const original = command && typeof command === "object" ? command : {};
- apps/watcher-api/src/server.mjs:624: let commandList;
- apps/watcher-api/src/server.mjs:627: commandList = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", fullPath];
- apps/watcher-api/src/server.mjs:630: commandList = ["D:/dev/autocode/ai-bridge/.venv/Scripts/python.exe", fullPath];
- apps/watcher-api/src/server.mjs:637: action: "run-command",
- apps/watcher-api/src/server.mjs:645: command: commandList,
- apps/watcher-api/src/server.mjs:652: function commandTimelinePercent(eventType) {
- apps/watcher-api/src/server.mjs:653: const key = String(eventType || "").toUpperCase();
- apps/watcher-api/src/server.mjs:656: QUEUED: 30,
- apps/watcher-api/src/server.mjs:657: CLAIMED_BY_GATEWAY: 60,
- apps/watcher-api/src/server.mjs:659: ACKED: 100,
- apps/watcher-api/src/server.mjs:666: async function insertBridgeCommandEvent(commandId, eventType, options = {}) {
- apps/watcher-api/src/server.mjs:667: const id = String(commandId || "").trim();
- apps/watcher-api/src/server.mjs:668: const type = String(eventType || "").trim();
- apps/watcher-api/src/server.mjs:673: percent: options.percent ?? commandTimelinePercent(type),
- apps/watcher-api/src/server.mjs:681: const result = await pool.query(
- apps/watcher-api/src/server.mjs:683: insert into bridge_command_events (
- apps/watcher-api/src/server.mjs:684: command_id,
- apps/watcher-api/src/server.mjs:685: event_type,
- apps/watcher-api/src/server.mjs:696: returning id, command_id, event_type, message, payload_json, created_at
- apps/watcher-api/src/server.mjs:712: return result.rows[0] || null;
- apps/watcher-api/src/server.mjs:715: async function commandTimeline(commandId) {
- apps/watcher-api/src/server.mjs:718: const id = String(commandId || "").trim();
- apps/watcher-api/src/server.mjs:719: if (!id) throw new Error("command_id_required");
- apps/watcher-api/src/server.mjs:721: const command = await pool.query(
- apps/watcher-api/src/server.mjs:723: select id, command_id, source_chat_id, target_chat_id, action, delivery_kind,
- apps/watcher-api/src/server.mjs:725: claimed_at, started_at, heartbeat_at, finished_at, acked_at, last_error
- apps/watcher-api/src/server.mjs:726: from bridge_commands
- apps/watcher-api/src/server.mjs:727: where command_id = $1
- apps/watcher-api/src/server.mjs:733: const events = await pool.query(
- apps/watcher-api/src/server.mjs:735: select id, command_id, event_type, runner_id, pid, return_code, duration_ms,
- apps/watcher-api/src/server.mjs:737: from bridge_command_events
- apps/watcher-api/src/server.mjs:738: where command_id = $1
- apps/watcher-api/src/server.mjs:745: command: command.rows[0] || null,
- apps/watcher-api/src/server.mjs:746: events: events.rows
- apps/watcher-api/src/server.mjs:750: async function insertBridgeCommand(command) {
- apps/watcher-api/src/server.mjs:752: command = normalizeBridgeCommandForInsert(command);
- apps/watcher-api/src/server.mjs:755: const commandId = String(command.command_id || "").trim();
- apps/watcher-api/src/server.mjs:756: const action = String(command.action || "").trim();
- apps/watcher-api/src/server.mjs:757: const targetChatId = canonicalChatId(command.target_chat_id);
- apps/watcher-api/src/server.mjs:758: const sourceChatId = canonicalChatId(command.source_chat_id || "");
- apps/watcher-api/src/server.mjs:759: const deliveryKind = String(command.delivery_kind || "inter_agent_message");
- apps/watcher-api/src/server.mjs:760: const conversationId = String(command.conversation_id || commandId);
- apps/watcher-api/src/server.mjs:761: const fromAgent = String(command.from_agent || "");
- apps/watcher-api/src/server.mjs:763: if (!commandId) throw new Error("command_id_required");
- apps/watcher-api/src/server.mjs:767: // API_SUPPRESS_REJECTION_REPLY_TO_WATCHER_API_20260608
- apps/watcher-api/src/server.mjs:768: const replyToCommandId = String(command.reply_to_command_id || command.replyToCommandId || "").trim();
- apps/watcher-api/src/server.mjs:769: const isApiRejectionReplyToWatcherApi =
- apps/watcher-api/src/server.mjs:770: action === "send-chat-message" &&
- apps/watcher-api/src/server.mjs:771: targetChatId === "watcher-api" &&
- apps/watcher-api/src/server.mjs:773: commandId.startsWith("reply_to_api_ingest_rejection_feedback_") ||
- apps/watcher-api/src/server.mjs:774: replyToCommandId.startsWith("api_ingest_rejection_feedback_") ||
- apps/watcher-api/src/server.mjs:775: conversationId === "api_ingest_rejection_feedback"
- apps/watcher-api/src/server.mjs:778: if (isApiRejectionReplyToWatcherApi) {
- apps/watcher-api/src/server.mjs:779: await insertBridgeCommandEvent(commandId, "SUPPRESSED", {
- apps/watcher-api/src/server.mjs:784: message: "suppressed api rejection reply to watcher-api",
- apps/watcher-api/src/server.mjs:786: reason: "api_rejection_feedback_replies_are_not_queued",
- apps/watcher-api/src/server.mjs:789: reply_to_command_id: replyToCommandId
- apps/watcher-api/src/server.mjs:796: command_id: commandId,
- apps/watcher-api/src/server.mjs:799: reason: "api_rejection_feedback_replies_are_not_queued"
- apps/watcher-api/src/server.mjs:805: const result = await client.query(
- apps/watcher-api/src/server.mjs:807: insert into bridge_commands (
- apps/watcher-api/src/broker.mjs:17: async function notifySourceChat(sourceChatId, commandId, stage, details = {}) {
- apps/watcher-api/src/broker.mjs:18: if (!brokerPool || !sourceChatId || !commandId) return;
- apps/watcher-api/src/broker.mjs:20: received: `BLUE[RECEBIDO] Comando ${commandId} recebido pelo broker e enfileirado.`,
- apps/watcher-api/src/broker.mjs:21: processing: `BLUE[PROCESSANDO] Comando ${commandId} em execucao...`,
- apps/watcher-api/src/broker.mjs:22: delivering: `BLUE[ENTREGANDO] Comando ${commandId} sendo enviado ao destino...`,
- apps/watcher-api/src/broker.mjs:23: delivered: `BLUE[ENTREGUE] Comando ${commandId} entregue ao chat destino.`,
- apps/watcher-api/src/broker.mjs:24: failed: `BLUE[FALHA] Comando ${commandId} falhou: ${details.error || 'erro desconhecido'}`,
- apps/watcher-api/src/broker.mjs:26: const message = messages[stage] || `BLUE[${stage}] ${commandId}`;
- apps/watcher-api/src/broker.mjs:29: `INSERT INTO ops.message_queue (queue_key, command_id, source_chat_id, target_chat_id, action, delivery_kind, from_agent, payload_text, payload_json, priority, status)
- apps/watcher-api/src/broker.mjs:30: VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, 'queued')`,
- apps/watcher-api/src/broker.mjs:31: [sourceChatId, `notify_${stage}_${commandId}`, 'system', sourceChatId, 'send-chat-message', 'lifecycle_notification', 'system', message, JSON.stringify({stage, commandId, ...details}), 10]
- apps/watcher-api/src/broker.mjs:40: const commandId = String(body.command_id || "msg_" + Date.now() + "_" + Math.random().toString(36).slice(2, 8));
- apps/watcher-api/src/broker.mjs:59: const isDuplicate = await checkDuplicate(commandId, targetChatId);
- apps/watcher-api/src/broker.mjs:65: const result = await brokerPool.query(
- apps/watcher-api/src/broker.mjs:66: `INSERT INTO ops.message_queue
- apps/watcher-api/src/broker.mjs:67: (queue_key, command_id, source_chat_id, target_chat_id, conversation_id, reply_to_id, correlation_id,
- apps/watcher-api/src/broker.mjs:70: ON CONFLICT (command_id, target_chat_id) WHERE status NOT IN ('failed', 'cancelled') DO NOTHING
- apps/watcher-api/src/broker.mjs:74: commandId,
- apps/watcher-api/src/broker.mjs:78: body.reply_to_command_id || null,
- apps/watcher-api/src/broker.mjs:79: body.correlation_id || commandId,
- apps/watcher-api/src/broker.mjs:80: body.action || "send-chat-message",
- apps/watcher-api/src/broker.mjs:89: if (result.rows.length > 0) {
- apps/watcher-api/src/broker.mjs:90: if (status === "delivered" || status === "acked") {
- apps/watcher-api/src/broker.mjs:91: notifySourceChat(msg.source_chat_id, msg.command_id, "delivered");
- apps/watcher-api/src/broker.mjs:94: await logMetric("message_ingested", { command_id: commandId, target_chat_id: targetChatId, priority });
- apps/watcher-api/src/broker.mjs:95: logMessageEvent(result.rows[0].id, commandId, "queued", sourceChatId, targetChatId, "cloud_broker", {priority});
- apps/watcher-api/src/broker.mjs:113: notifySourceChat(sourceChatId, commandId, "received");
- apps/watcher-api/src/broker.mjs:114: return { ok: true, ingested: true, id: result.rows[0].id, command_id: commandId, priority };
- apps/watcher-api/src/broker.mjs:127: // SMART CLAIM (with priority, ordering, batching)
- apps/watcher-api/src/broker.mjs:130: export async function smartClaim(targetChatId, instanceId, options = {}) {
- apps/watcher-api/src/broker.mjs:140: // Cleanup stale claims first
- apps/watcher-api/src/broker.mjs:143: // Claim messages with priority ordering + SKIP LOCKED for parallelism
- apps/watcher-api/src/broker.mjs:144: const result = await client.query(
- apps/watcher-api/src/broker.mjs:145: `SELECT id, command_id, source_chat_id, payload_text, payload_json,
- apps/watcher-api/src/broker.mjs:147: FROM ops.message_queue
- apps/watcher-api/src/broker.mjs:149: AND status = 'queued'
- apps/watcher-api/src/broker.mjs:150: AND (claim_expires_at IS NULL OR claim_expires_at < now())
- apps/watcher-api/src/broker.mjs:157: if (result.rows.length === 0) {
- apps/watcher-api/src/broker.mjs:159: return { ok: true, messages: [], queue_empty: true };
- apps/watcher-api/src/broker.mjs:162: // Mark as claimed with expiration
- apps/watcher-api/src/broker.mjs:163: const ids = result.rows.map(r => r.id);
- apps/watcher-api/src/broker.mjs:165: `UPDATE ops.message_queue
- apps/watcher-api/src/broker.mjs:166: SET status = 'claimed',
- apps/watcher-api/src/broker.mjs:167: claim_instance = $2,
- apps/watcher-api/src/broker.mjs:168: claim_expires_at = now() + INTERVAL '30 seconds',
- apps/watcher-api/src/broker.mjs:169: claimed_at = now(),
- apps/watcher-api/src/broker.mjs:178: if (status === "delivered" || status === "acked") {
- apps/watcher-api/src/broker.mjs:179: notifySourceChat(msg.source_chat_id, msg.command_id, "delivered");
- apps/watcher-api/src/broker.mjs:182: notifySourceChat(msg.source_chat_id, msg.command_id, "processing");
- apps/watcher-api/src/broker.mjs:183: await logMetric("messages_claimed", { count: ids.length, target_chat_id: targetChatId, instance: instanceId });
- apps/watcher-api/src/broker.mjs:187: messages: result.rows.map(r => ({
- apps/watcher-api/src/broker.mjs:189: command_id: r.command_id,
- apps/watcher-api/src/broker.mjs:199: count: result.rows.length
- apps/watcher-api/src/broker.mjs:202: await client.query("ROLLBACK");
- apps/watcher-api/src/broker.mjs:210: // ACK / STATUS UPDATE
- apps/watcher-api/src/broker.mjs:216: const validStatuses = ["delivered", "acked", "failed", "cancelled"];
- apps/watcher-api/src/broker.mjs:222: const timestamp = status === "delivered" ? "delivered_at" : status === "acked" ? "acked_at" : null;
- apps/watcher-api/src/broker.mjs:226: `UPDATE ops.message_queue
- apps/watcher-api/src/broker.mjs:233: logMessageEvent(messageId, "", status, "", "", "cloud_broker", {error: errorText}); return { ok: true };
- apps/watcher-api/src/broker.mjs:243: async function logMessageEvent(messageId, commandId, eventType, sourceChatId, targetChatId, adapter, metadata) { if (!brokerPool) return; try { await brokerPool.query(`INSERT INTO ops.message_log (message_id, command_id, event_type, source_chat_id, target_chat
- apps/watcher-api/src/broker.mjs:255: export async function getQueueStats(targetChatId = null) {
- apps/watcher-api/src/broker.mjs:262: AVG(EXTRACT(EPOCH FROM (claimed_at - created_at))) * 1000 as avg_latency_ms
- apps/watcher-api/src/broker.mjs:263: FROM ops.message_queue
- apps/watcher-api/src/broker.mjs:275: const result = await brokerPool.query(query, params);
- apps/watcher-api/src/broker.mjs:276: return { ok: true, stats: result.rows };
- apps/watcher-api/src/broker.mjs:288: if (body.reply_to_command_id) return 2; // Replies are important
- apps/watcher-api/src/broker.mjs:296: const result = await brokerPool.query(
- apps/watcher-api/src/broker.mjs:297: `SELECT COUNT(*) as count FROM ops.message_queue
- apps/watcher-api/src/broker.mjs:301: const count = parseInt(result.rows[0]?.count || 0);
- apps/watcher-api/src/broker.mjs:312: async function checkDuplicate(commandId, targetChatId) {
- apps/watcher-api/src/broker.mjs:314: const result = await brokerPool.query(
- apps/watcher-api/src/broker.mjs:315: `SELECT id FROM ops.message_queue
- apps/watcher-api/src/broker.mjs:316: WHERE command_id = $1 AND target_chat_id = $2
- apps/watcher-api/src/broker.mjs:319: [commandId, targetChatId]
- apps/watcher-api/src/broker.mjs:321: return result.rows.length > 0;
- apps/watcher-api/src/message-queue.mjs:1: // MESSAGE_QUEUE_V1 - Parallel Multi-Chat Queue
- apps/watcher-api/src/message-queue.mjs:2: // Uses ops.message_queue with FOR UPDATE SKIP LOCKED
- apps/watcher-api/src/message-queue.mjs:4: let queuePool = null;
- apps/watcher-api/src/message-queue.mjs:6: export function setQueuePool(pool) {
- apps/watcher-api/src/message-queue.mjs:7: queuePool = pool;
- apps/watcher-api/src/message-queue.mjs:10: // Enqueue a message for delivery
- apps/watcher-api/src/message-queue.mjs:11: export async function enqueueMessage(body) {
- apps/watcher-api/src/message-queue.mjs:12: if (!queuePool) return { error: "pool_not_available" };
- apps/watcher-api/src/message-queue.mjs:14: const commandId = String(body.command_id || "msg_" + Date.now() + "_" + Math.random().toString(36).slice(2, 8));
- apps/watcher-api/src/message-queue.mjs:21: const result = await queuePool.query(
- apps/watcher-api/src/message-queue.mjs:22: `INSERT INTO ops.message_queue
- apps/watcher-api/src/message-queue.mjs:23: (queue_key, command_id, source_chat_id, target_chat_id, conversation_id, reply_to_id, correlation_id,
- apps/watcher-api/src/message-queue.mjs:26: ON CONFLICT (command_id, target_chat_id) WHERE status NOT IN ('failed', 'cancelled') DO NOTHING
- apps/watcher-api/src/message-queue.mjs:30: commandId,
- apps/watcher-api/src/message-queue.mjs:34: body.reply_to_command_id || null,
- apps/watcher-api/src/message-queue.mjs:36: body.action || "send-chat-message",
- apps/watcher-api/src/message-queue.mjs:45: if (result.rows.length > 0) {
- apps/watcher-api/src/message-queue.mjs:46: return { ok: true, enqueued: true, id: result.rows[0].id, command_id: commandId };
- apps/watcher-api/src/message-queue.mjs:48: return { ok: true, enqueued: false, reason: "duplicate" };
- apps/watcher-api/src/message-queue.mjs:55: // Claim the next message for a specific chat (PARALLEL SAFE)
- apps/watcher-api/src/message-queue.mjs:56: export async function claimNextMessage(targetChatId, instanceId) {
- apps/watcher-api/src/message-queue.mjs:57: if (!queuePool) return { error: "pool_not_available" };
- apps/watcher-api/src/message-queue.mjs:60: const client = await queuePool.connect();
- apps/watcher-api/src/message-queue.mjs:65: const result = await client.query(
- apps/watcher-api/src/message-queue.mjs:66: `SELECT id, command_id, source_chat_id, payload_text, payload_json, delivery_kind,
- apps/watcher-api/src/message-queue.mjs:68: FROM ops.message_queue
- apps/watcher-api/src/message-queue.mjs:70: AND status = 'queued'
- apps/watcher-api/src/message-queue.mjs:71: AND (claim_expires_at IS NULL OR claim_expires_at < now())
- apps/watcher-api/src/message-queue.mjs:78: if (result.rows.length === 0) {
- apps/watcher-api/src/message-queue.mjs:83: const msg = result.rows[0];
- apps/watcher-api/src/message-queue.mjs:85: // Mark as claimed
- apps/watcher-api/src/message-queue.mjs:87: `UPDATE ops.message_queue
- apps/watcher-api/src/message-queue.mjs:88: SET status = 'claimed',
- apps/watcher-api/src/message-queue.mjs:89: claim_instance = $2,
- apps/watcher-api/src/message-queue.mjs:90: claim_expires_at = now() + INTERVAL '30 seconds',
- apps/watcher-api/src/message-queue.mjs:91: claimed_at = now(),
- apps/watcher-api/src/message-queue.mjs:95: [msg.id, instanceId || "watcher-api"]
- apps/watcher-api/src/message-queue.mjs:104: command_id: msg.command_id,
- apps/watcher-api/src/message-queue.mjs:116: await client.query("ROLLBACK");
- apps/watcher-api/src/message-queue.mjs:123: // Ack delivery (mark as delivered/acked)
- apps/watcher-api/src/message-queue.mjs:124: export async function ackMessage(messageId, status = "delivered") {
- apps/watcher-api/src/message-queue.mjs:125: if (!queuePool) return { error: "pool_not_available" };
- apps/watcher-api/src/message-queue.mjs:129: await queuePool.query(
- apps/watcher-api/src/message-queue.mjs:130: `UPDATE ops.message_queue
- apps/watcher-api/src/message-queue.mjs:132: ${status === "delivered" ? "delivered_at" : "acked_at"} = now(),

## Working model

The expected model for WS AI Office is:

    WS AI Office Railway API
        -> command/task/approval records
        -> AI Bridge compatible gateway contract
        -> ai-bridge local/browser gateway
        -> result/event/ACK back to Railway API

## Safety constraints

- No local command execution integration yet.
- No mutation of ai-bridge.
- No secrets copied into WS AI Office docs.
- Any execution path must wait for approval gates.
- Any gateway integration must have readonly smoke first.

## Next questions

- What exact endpoint does the local/browser gateway poll?
- What exact endpoint receives delivery ACK?
- What exact endpoint receives execution result?
- What is the JSON envelope shape?
- Which statuses are final, retryable or failed?
- Which pieces should WS AI Office reproduce versus call through compatibility endpoints?

## Recommended next micro

Read only the most relevant source files and extract route definitions plus envelope shapes from apps/watcher-api/src/server.mjs and extension-next/background.js.
