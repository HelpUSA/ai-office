# WS AI Office Phase B Gateway Contract Evidence

Status: readonly evidence extraction only.

This document was generated from local AI Bridge source files without enabling gateway integration, command execution, ACK, queue claim, database writes, file operations or git operations.

## Source roots

- WS AI Office: `D:\dev\autocode\ai-office`
- AI Bridge reference: `D:\dev\autocode\ai-bridge`

## Safety assertion

- Readonly source inspection only.
- No AI Bridge process started.
- No route called.
- No queue polled.
- No ACK posted.
- No command created.
- No local execution enabled.

## Files inspected

- present: `apps/watcher-api/src/server.mjs`
- present: `apps/watcher-api/src/message-queue.mjs`
- present: `apps/watcher-api/src/broker.mjs`
- present: `extension-next/background.js`
- present: `extension-next/content_script.js`
- present: `extension-next/capability_router.js`

## Route evidence

| method | route | file | line | evidence |
|---|---|---|---|---|
| unknown | /bridge/next-action | apps/watcher-api/src/server.mjs | 2099 | if (req.method === "GET" && url.pathname === "/bridge/next-action") { |
| unknown | /bridge/acks | apps/watcher-api/src/server.mjs | 2296 | if (req.method === "POST" && url.pathname === "/bridge/acks") { |
| unknown | /ack | apps/watcher-api/src/server.mjs | 2296 | if (req.method === "POST" && url.pathname === "/bridge/acks") { |
| unknown | /bridge/events | apps/watcher-api/src/server.mjs | 2329 | if (req.method === "POST" && url.pathname === "/bridge/events") { |
| unknown | /claim | apps/watcher-api/src/server.mjs | 2430 | if (req.method === "GET" && url.pathname === "/claim") { |
| unknown | /ack | apps/watcher-api/src/server.mjs | 2440 | if (req.method === "POST" && url.pathname === "/ack") { |
| unknown | /claim | apps/watcher-api/src/server.mjs | 2463 | if (req.method === "GET" && url.pathname === "/claim") { |
| unknown | /ack | apps/watcher-api/src/server.mjs | 2466 | if (req.method === "POST" && url.pathname === "/ack") { |
| unknown | /ack | apps/watcher-api/src/message-queue.mjs | 123 | // Ack delivery (mark as delivered/acked) |
| unknown | /bridge/events | extension-next/background.js | 201 | // POST_EVENT_USES_BRIDGE_EVENTS_20260609: server endpoint is /bridge/events, not legacy /event. |
| unknown | /bridge/events | extension-next/background.js | 202 | await fetch(`${GATEWAY_BASE}/bridge/events`, { |
| unknown | /bridge/acks | extension-next/background.js | 371 | // /bridge/acks from the extension means browser transport/delivery was attempted. |
| unknown | /ack | extension-next/background.js | 371 | // /bridge/acks from the extension means browser transport/delivery was attempted. |
| unknown | /bridge/acks | extension-next/background.js | 383 | const result = await cloudFetchJson("/bridge/acks", { |
| unknown | /ack | extension-next/background.js | 383 | const result = await cloudFetchJson("/bridge/acks", { |
| unknown | /bridge/next-action | extension-next/background.js | 589 | const result = await cloudFetchJson(`/bridge/next-action?chat_id=${encodeURIComponent(normalizedChatId)}`, { |
| unknown | /bridge/next-action | extension-next/background.js | 607 | // CLOUD_GATEWAY_NEXT_ACTION_RECEIVED_20260609: observable event immediately after /bridge/next-action returns an action. |
| unknown | /bridge/next-action | extension-next/background.js | 707 | // Do not claim another /bridge/next-action immediately for the same chat. |
| unknown | /bridge/next-action | extension-next/background.js | 716 | const nextResult = await cloudFetchJson(`/bridge/next-action?chat_id=${encodeURIComponent(normalizedChatId)}`, { |
| unknown | /bridge/events | extension-next/content_script.js | 68 | return config.useCloud ? (config.cloudBase + "/bridge/events") : (GATEWAY_BASE + "/event"); |

## Field evidence

| field | file | line | evidence |
|---|---|---|---|
| status | apps/watcher-api/src/server.mjs | 2 | import { createHash } from "node:crypto"; import { Pool } from "pg"; import { handleGitOp } from "./git-op.mjs"; import { handleCodexAnalyze } from "./codex-analyze.mjs"; import... |
| action | apps/watcher-api/src/server.mjs | 11 | // GIT_OP_CLOUD_ACTION_V2 - imported from ./git-op.mjs |
| payload | apps/watcher-api/src/server.mjs | 103 | function sanitizedDatabaseDebugPayload() { |
| payload | apps/watcher-api/src/server.mjs | 104 | const payload = { |
| payload | apps/watcher-api/src/server.mjs | 119 | payload.db_host = process.env.PGHOST \|\| null; |
| payload | apps/watcher-api/src/server.mjs | 120 | payload.db_port = process.env.PGPORT \|\| null; |
| payload | apps/watcher-api/src/server.mjs | 121 | payload.db_name = process.env.PGDATABASE \|\| null; |
| payload | apps/watcher-api/src/server.mjs | 122 | payload.url_sslmode = null; |
| payload | apps/watcher-api/src/server.mjs | 123 | payload.effective_ssl = process.env.PGSSLMODE === "require" ? "enabled" : "disabled"; |
| payload | apps/watcher-api/src/server.mjs | 124 | return payload; |
| payload | apps/watcher-api/src/server.mjs | 127 | if (!databaseUrl) return payload; |
| payload | apps/watcher-api/src/server.mjs | 131 | payload.db_host = url.hostname \|\| null; |
| payload | apps/watcher-api/src/server.mjs | 132 | payload.db_port = url.port \|\| null; |
| payload | apps/watcher-api/src/server.mjs | 133 | payload.db_name = url.pathname ? url.pathname.replace(/^\//, "") : null; |
| payload | apps/watcher-api/src/server.mjs | 134 | payload.url_sslmode = url.searchParams.get("sslmode"); |
| failed | apps/watcher-api/src/server.mjs | 136 | payload.db_host = "parse_failed"; |
| payload | apps/watcher-api/src/server.mjs | 140 | payload.effective_ssl = ssl === false ? "disabled" : "enabled"; |
| payload | apps/watcher-api/src/server.mjs | 142 | return payload; |
| error | apps/watcher-api/src/server.mjs | 148 | function safeDbProbeError(error) { |
| error | apps/watcher-api/src/server.mjs | 150 | name: error?.name \|\| null, |
| error | apps/watcher-api/src/server.mjs | 151 | code: error?.code \|\| null, |
| error | apps/watcher-api/src/server.mjs | 152 | message: safeError(error) |
| result | apps/watcher-api/src/server.mjs | 171 | function timeoutResult(name, startedAt, timeoutMs) { |
| error | apps/watcher-api/src/server.mjs | 177 | error: { |
| result | apps/watcher-api/src/server.mjs | 193 | const result = await probePool.query("select 1::int as ok"); |
| result | apps/watcher-api/src/server.mjs | 198 | row_ok: result.rows?.[0]?.ok === 1 |
| error | apps/watcher-api/src/server.mjs | 200 | } catch (error) { |
| error | apps/watcher-api/src/server.mjs | 205 | error: safeDbProbeError(error) |
| result | apps/watcher-api/src/server.mjs | 211 | timer = setTimeout(() => resolve(timeoutResult(name, startedAt, timeoutMs)), timeoutMs); |
| payload | apps/watcher-api/src/server.mjs | 224 | async function sanitizedDatabaseProbePayload() { |
| result | apps/watcher-api/src/server.mjs | 292 | const result = await client.query("select now() as now, current_database() as database"); |
| result | apps/watcher-api/src/server.mjs | 293 | return { ok: true, ...result.rows[0] }; |
| error | apps/watcher-api/src/server.mjs | 299 | function safeError(error) { |
| error | apps/watcher-api/src/server.mjs | 300 | const message = error instanceof Error ? error.message : String(error); |
| failed | apps/watcher-api/src/server.mjs | 301 | return message.includes("://") ? "database_check_failed" : message; |
| status | apps/watcher-api/src/server.mjs | 304 | function writeJson(res, statusCode, payload) { |
| status | apps/watcher-api/src/server.mjs | 305 | res.writeHead(statusCode, { |
| type | apps/watcher-api/src/server.mjs | 306 | "content-type": "application/json; charset=utf-8", |
| payload | apps/watcher-api/src/server.mjs | 309 | res.end(JSON.stringify(payload, null, 2) + "\n"); |
| error | apps/watcher-api/src/server.mjs | 339 | reject(new Error("json_body_too_large")); |
| error | apps/watcher-api/src/server.mjs | 355 | reject(new Error("malformed_json")); |
| error | apps/watcher-api/src/server.mjs | 359 | req.on("error", reject); |
| text | apps/watcher-api/src/server.mjs | 367 | alter table if exists brain.facts add column if not exists fact_key text; |
| type | apps/watcher-api/src/server.mjs | 368 | alter table if exists brain.facts add column if not exists fact_type text; |
| chat_id | apps/watcher-api/src/server.mjs | 369 | alter table if exists brain.facts add column if not exists chat_id text; |
| text | apps/watcher-api/src/server.mjs | 371 | alter table if exists brain.facts add column if not exists severity text not null default 'info'; |
| text | apps/watcher-api/src/server.mjs | 372 | alter table if exists brain.facts add column if not exists title text; |
| text | apps/watcher-api/src/server.mjs | 373 | alter table if exists brain.facts add column if not exists fact_text text; |
| text | apps/watcher-api/src/server.mjs | 374 | alter table if exists brain.facts add column if not exists evidence text; |
| created_at | apps/watcher-api/src/server.mjs | 377 | alter table if exists brain.facts add column if not exists created_at timestamptz not null default now(); |
| type | apps/watcher-api/src/server.mjs | 379 | update brain.facts set fact_key = coalesce(fact_key, md5(coalesce(chat_id,'') \|\| coalesce(fact_type,'') \|\| coalesce(fact_text,'') \|\| id::text)) where fact_key is null; |
| type | apps/watcher-api/src/server.mjs | 380 | update brain.facts set fact_type = coalesce(fact_type, 'legacy') where fact_type is null; |
| text | apps/watcher-api/src/server.mjs | 381 | update brain.facts set fact_text = coalesce(fact_text, evidence, title, 'legacy fact') where fact_text is null; |
| error | apps/watcher-api/src/server.mjs | 394 | throw new Error("database_url_missing"); |
| chat_id | apps/watcher-api/src/server.mjs | 404 | chat_id text not null, |
| text | apps/watcher-api/src/server.mjs | 405 | platform text, |
| text | apps/watcher-api/src/server.mjs | 406 | url text, |
| text | apps/watcher-api/src/server.mjs | 407 | title text, |
| text | apps/watcher-api/src/server.mjs | 409 | last_message_hash text not null, |
| created_at | apps/watcher-api/src/server.mjs | 411 | created_at timestamptz not null default now(), |
| chat_id | apps/watcher-api/src/server.mjs | 413 | unique (chat_id, last_message_hash) |
| chat_id | apps/watcher-api/src/server.mjs | 416 | await client.query(`create index if not exists brain_conversation_snapshots_chat_created_idx on brain.conversation_snapshots (chat_id, created_at desc)`); |
| chat_id | apps/watcher-api/src/server.mjs | 422 | chat_id text not null, |
| type | apps/watcher-api/src/server.mjs | 424 | fact_type text not null, |
| text | apps/watcher-api/src/server.mjs | 425 | severity text not null default 'info', |
| status | apps/watcher-api/src/server.mjs | 426 | status text not null default 'open', |
| text | apps/watcher-api/src/server.mjs | 428 | title text, |
| text | apps/watcher-api/src/server.mjs | 429 | summary text, |
| text | apps/watcher-api/src/server.mjs | 431 | dedupe_key text not null, |
| text | apps/watcher-api/src/server.mjs | 432 | source text not null default 'semantic_worker_v1', |
| status | apps/watcher-api/src/server.mjs | 439 | await client.query(`create index if not exists brain_facts_status_severity_last_seen_idx on brain.facts (status, severity, last_seen_at desc)`); |
| chat_id | apps/watcher-api/src/server.mjs | 440 | await client.query(`create index if not exists brain_facts_chat_last_seen_idx on brain.facts (chat_id, last_seen_at desc)`); |
| command | apps/watcher-api/src/server.mjs | 443 | create table if not exists bridge_commands ( |
| command_id | apps/watcher-api/src/server.mjs | 445 | command_id text not null unique, |
| source_chat_id | apps/watcher-api/src/server.mjs | 446 | source_chat_id text, |
| target_chat_id | apps/watcher-api/src/server.mjs | 447 | target_chat_id text not null, |
| action | apps/watcher-api/src/server.mjs | 448 | action text not null, |
| delivery_kind | apps/watcher-api/src/server.mjs | 449 | delivery_kind text, |
| conversation_id | apps/watcher-api/src/server.mjs | 450 | conversation_id text, |
| text | apps/watcher-api/src/server.mjs | 451 | from_agent text, |
| payload | apps/watcher-api/src/server.mjs | 452 | payload_json jsonb not null, |
| status | apps/watcher-api/src/server.mjs | 453 | status text not null default 'queued', |
| attempts | apps/watcher-api/src/server.mjs | 454 | delivery_attempts integer not null default 0, |
| created_at | apps/watcher-api/src/server.mjs | 455 | created_at timestamptz not null default now(), |
| delivered | apps/watcher-api/src/server.mjs | 456 | delivered_at timestamptz, |
| acked | apps/watcher-api/src/server.mjs | 457 | acked_at timestamptz, |
| last_error | apps/watcher-api/src/server.mjs | 458 | last_error text |
| status | apps/watcher-api/src/server.mjs | 463 | create index if not exists bridge_commands_target_status_created_idx |
| target_chat_id | apps/watcher-api/src/server.mjs | 464 | on bridge_commands (target_chat_id, status, created_at) |
| command | apps/watcher-api/src/server.mjs | 469 | alter table bridge_commands add column if not exists claimed_at timestamptz, |
| text | apps/watcher-api/src/server.mjs | 475 | add column if not exists runner_id text, |
| text | apps/watcher-api/src/server.mjs | 477 | add column if not exists stdout_tail text, |
| text | apps/watcher-api/src/server.mjs | 478 | add column if not exists stderr_tail text, |
| text | apps/watcher-api/src/server.mjs | 479 | add column if not exists last_progress_message text |
| command | apps/watcher-api/src/server.mjs | 483 | create table if not exists bridge_command_events ( |
| command_id | apps/watcher-api/src/server.mjs | 485 | command_id text not null, |
| type | apps/watcher-api/src/server.mjs | 486 | event_type text not null, |
| text | apps/watcher-api/src/server.mjs | 487 | runner_id text, |
| text | apps/watcher-api/src/server.mjs | 491 | stdout_tail text, |
| text | apps/watcher-api/src/server.mjs | 492 | stderr_tail text, |
| text | apps/watcher-api/src/server.mjs | 493 | message text, |
| payload | apps/watcher-api/src/server.mjs | 494 | payload_json jsonb, |
| created_at | apps/watcher-api/src/server.mjs | 495 | created_at timestamptz not null default now() |
| chat_id | apps/watcher-api/src/server.mjs | 501 | chat_id text, |
| text | apps/watcher-api/src/server.mjs | 502 | source text, |
| text | apps/watcher-api/src/server.mjs | 503 | kind text not null, |
| payload | apps/watcher-api/src/server.mjs | 504 | payload_json jsonb not null, |
| created_at | apps/watcher-api/src/server.mjs | 505 | created_at timestamptz not null default now() |
| chat_id | apps/watcher-api/src/server.mjs | 511 | on bridge_events (chat_id, created_at) |
| command_id | apps/watcher-api/src/server.mjs | 517 | SELECT parent.command_id AS original_command_id, |
| source_chat_id | apps/watcher-api/src/server.mjs | 518 | parent.source_chat_id AS waiting_chat_id, |
| target_chat_id | apps/watcher-api/src/server.mjs | 519 | parent.target_chat_id AS requested_chat_id, |
| conversation_id | apps/watcher-api/src/server.mjs | 520 | parent.conversation_id, |
| delivery_kind | apps/watcher-api/src/server.mjs | 521 | parent.delivery_kind, |
| payload | apps/watcher-api/src/server.mjs | 523 | COALESCE(parent.payload_json->>'message', parent.payload_json->>'text', '') AS original_message, |
| created_at | apps/watcher-api/src/server.mjs | 524 | parent.created_at AS original_created_at, |
| created_at | apps/watcher-api/src/server.mjs | 525 | EXTRACT(EPOCH FROM (now() - parent.created_at))::int AS age_seconds |
| command | apps/watcher-api/src/server.mjs | 526 | FROM bridge_commands parent |
| delivery_kind | apps/watcher-api/src/server.mjs | 527 | WHERE parent.delivery_kind = 'inter_agent_message' |
| source_chat_id | apps/watcher-api/src/server.mjs | 528 | AND parent.source_chat_id IS NOT NULL |
| target_chat_id | apps/watcher-api/src/server.mjs | 529 | AND parent.target_chat_id IS NOT NULL |
| status | apps/watcher-api/src/server.mjs | 530 | AND parent.status IN ('queued','retry','processing','delivered') |
| command | apps/watcher-api/src/server.mjs | 532 | SELECT 1 FROM bridge_commands reply |
| command_id | apps/watcher-api/src/server.mjs | 533 | WHERE (reply.payload_json->>'reply_to_command_id') = parent.command_id |
| source_chat_id | apps/watcher-api/src/server.mjs | 534 | AND reply.source_chat_id = parent.target_chat_id |
| source_chat_id | apps/watcher-api/src/server.mjs | 535 | AND reply.target_chat_id = parent.source_chat_id |
| chat_id | apps/watcher-api/src/server.mjs | 541 | chat_id text primary key, |
| text | apps/watcher-api/src/server.mjs | 542 | platform text, |
| text | apps/watcher-api/src/server.mjs | 545 | last_source text, |
| chat_id | apps/watcher-api/src/server.mjs | 552 | alter table if exists app.chat_threads add column if not exists chat_id text; |
| text | apps/watcher-api/src/server.mjs | 553 | alter table if exists app.chat_threads add column if not exists platform text; |
| text | apps/watcher-api/src/server.mjs | 556 | alter table if exists app.chat_threads add column if not exists last_source text; |
| chat_id | apps/watcher-api/src/server.mjs | 558 | create unique index if not exists app_chat_threads_chat_id_uidx |
| chat_id | apps/watcher-api/src/server.mjs | 559 | on app.chat_threads (chat_id); |
| chat_id | apps/watcher-api/src/server.mjs | 566 | chat_id text not null, |
| text | apps/watcher-api/src/server.mjs | 567 | direction text, |
| text | apps/watcher-api/src/server.mjs | 568 | role text, |
| text | apps/watcher-api/src/server.mjs | 569 | source text, |
| text | apps/watcher-api/src/server.mjs | 570 | kind text, |
| text | apps/watcher-api/src/server.mjs | 571 | message_text text, |
| conversation_id | apps/watcher-api/src/server.mjs | 572 | conversation_id text, |
| command_id | apps/watcher-api/src/server.mjs | 573 | command_id text, |
| payload | apps/watcher-api/src/server.mjs | 574 | payload_json jsonb not null, |
| created_at | apps/watcher-api/src/server.mjs | 575 | created_at timestamptz not null default now() |
| chat_id | apps/watcher-api/src/server.mjs | 587 | on app.chat_messages (chat_id, created_at) |
| command | apps/watcher-api/src/server.mjs | 595 | function normalizeBridgeCommandForInsert(command) { |
| type | apps/watcher-api/src/server.mjs | 596 | const original = command && typeof command === "object" ? command : {}; |
| action | apps/watcher-api/src/server.mjs | 597 | const action = String(original.action \|\| "").trim(); |
| action | apps/watcher-api/src/server.mjs | 599 | if (action !== "run-template") { |
| type | apps/watcher-api/src/server.mjs | 603 | const payload = original.payload && typeof original.payload === "object" ? original.payload : {}; |
| payload | apps/watcher-api/src/server.mjs | 604 | const templateId = String(payload.template_id \|\| original.template_id \|\| "").trim(); |
| payload | apps/watcher-api/src/server.mjs | 605 | const scriptPathRaw = String(payload.script_path \|\| original.script_path \|\| "").trim(); |
| payload | apps/watcher-api/src/server.mjs | 606 | const cwd = String(payload.cwd \|\| original.cwd \|\| "D:/dev/autocode/ai-bridge").trim(); |
| payload | apps/watcher-api/src/server.mjs | 607 | const timeoutSeconds = Number(payload.timeout_seconds \|\| original.timeout_seconds \|\| 90); |
| error | apps/watcher-api/src/server.mjs | 610 | throw new Error("run_template_requires_template_id"); |
| error | apps/watcher-api/src/server.mjs | 614 | throw new Error(`unsupported_template_id:${templateId}`); |
| error | apps/watcher-api/src/server.mjs | 618 | throw new Error("run_script_requires_script_path"); |
| command | apps/watcher-api/src/server.mjs | 624 | let commandList; |
| command | apps/watcher-api/src/server.mjs | 627 | commandList = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", fullPath]; |
| command | apps/watcher-api/src/server.mjs | 630 | commandList = ["D:/dev/autocode/ai-bridge/.venv/Scripts/python.exe", fullPath]; |
| ... | ... | ... | ... |
| truncated | showing 160 of 2016 rows | | |

## Status lifecycle evidence

| status | file | line | evidence |
|---|---|---|---|
| failed | apps/watcher-api/src/server.mjs | 136 | payload.db_host = "parse_failed"; |
| failed | apps/watcher-api/src/server.mjs | 301 | return message.includes("://") ? "database_check_failed" : message; |
| queued | apps/watcher-api/src/server.mjs | 453 | status text not null default 'queued', |
| delivered | apps/watcher-api/src/server.mjs | 456 | delivered_at timestamptz, |
| acked | apps/watcher-api/src/server.mjs | 457 | acked_at timestamptz, |
| queued | apps/watcher-api/src/server.mjs | 530 | AND parent.status IN ('queued','retry','processing','delivered') |
| queued | apps/watcher-api/src/server.mjs | 656 | QUEUED: 30, |
| acked | apps/watcher-api/src/server.mjs | 659 | ACKED: 100, |
| failed | apps/watcher-api/src/server.mjs | 661 | FAILED: 100 |
| delivered | apps/watcher-api/src/server.mjs | 724 | conversation_id, status, delivery_attempts, created_at, delivered_at, |
| acked | apps/watcher-api/src/server.mjs | 725 | claimed_at, started_at, heartbeat_at, finished_at, acked_at, last_error |
| queued | apps/watcher-api/src/server.mjs | 786 | reason: "api_rejection_feedback_replies_are_not_queued", |
| queued | apps/watcher-api/src/server.mjs | 799 | reason: "api_rejection_feedback_replies_are_not_queued" |
| queued | apps/watcher-api/src/server.mjs | 818 | values ($1,$2,$3,$4,$5,$6,$7,$8::jsonb,'queued') |
| queued | apps/watcher-api/src/server.mjs | 836 | await insertBridgeCommandEvent(commandId, "QUEUED", { |
| queued | apps/watcher-api/src/server.mjs | 840 | status: row?.status \|\| "queued", |
| queued | apps/watcher-api/src/server.mjs | 841 | message: "command queued by API", |
| failed | apps/watcher-api/src/server.mjs | 957 | add("error_detected", "error", "Error or failure signal detected.", /(traceback\|exception\|error\|erro\|failed\|failure\|falhou\|rejected\|malformed\|timeout\|NameError\|TypeEr... |
| queued | apps/watcher-api/src/server.mjs | 958 | add("task_completed", "info", "Completion or success signal detected.", /(TASK_DONE\|DISPATCH_QUEUED\|commit\|push\|acked\|concluido\|concluÃƒÂ­do\|feito\|done\|passed\|ok": tru... |
| running | apps/watcher-api/src/server.mjs | 991 | let brainSemanticWorkerRunning = false; |
| running | apps/watcher-api/src/server.mjs | 993 | if (brainSemanticWorkerRunning) return; |
| running | apps/watcher-api/src/server.mjs | 994 | brainSemanticWorkerRunning = true; |
| running | apps/watcher-api/src/server.mjs | 1000 | brainSemanticWorkerRunning = false; |
| queued | apps/watcher-api/src/server.mjs | 1040 | and status in ('queued', 'retry') |
| delivered | apps/watcher-api/src/server.mjs | 1060 | delivered_at = now(), |
| queued | apps/watcher-api/src/server.mjs | 1101 | async function cancelStaleQueuedCommands(body = {}) { |
| queued | apps/watcher-api/src/server.mjs | 1114 | where status = 'queued' |
| failed | apps/watcher-api/src/server.mjs | 1137 | set status = 'failed', |
| acked | apps/watcher-api/src/server.mjs | 1138 | acked_at = coalesce(acked_at, now()), |
| queued | apps/watcher-api/src/server.mjs | 1139 | last_error = concat_ws('; ', nullif(last_error, ''), 'cancelled_stale_queued') |
| queued | apps/watcher-api/src/server.mjs | 1143 | where status = 'queued' |
| delivered | apps/watcher-api/src/server.mjs | 1163 | async function autoAckStaleDeliveredCommands(body = {}) { |
| delivered | apps/watcher-api/src/server.mjs | 1174 | select command_id, action, target_chat_id, status, delivered_at, acked_at |
| acked | apps/watcher-api/src/server.mjs | 1179 | -- AUTO_ACK_EXCLUDE_SEND_CHAT_MESSAGE_20260608: send-chat-message must be recovered/retried, not auto-acked. |
| delivered | apps/watcher-api/src/server.mjs | 1181 | and delivered_at is not null |
| delivered | apps/watcher-api/src/server.mjs | 1182 | and delivered_at < now() - ($1::int * interval '1 minute') |
| delivered | apps/watcher-api/src/server.mjs | 1183 | order by delivered_at asc |
| acked | apps/watcher-api/src/server.mjs | 1204 | set status = 'acked', |
| acked | apps/watcher-api/src/server.mjs | 1205 | acked_at = coalesce(acked_at, now()), |
| delivered | apps/watcher-api/src/server.mjs | 1206 | last_error = concat_ws('; ', nullif(last_error, ''), 'auto_ack_stale_delivered') |
| acked | apps/watcher-api/src/server.mjs | 1213 | -- AUTO_ACK_EXCLUDE_SEND_CHAT_MESSAGE_20260608: send-chat-message must be recovered/retried, not auto-acked. |
| delivered | apps/watcher-api/src/server.mjs | 1215 | and delivered_at is not null |
| delivered | apps/watcher-api/src/server.mjs | 1216 | and delivered_at < now() - ($1::int * interval '1 minute') |
| delivered | apps/watcher-api/src/server.mjs | 1217 | order by delivered_at asc |
| delivered | apps/watcher-api/src/server.mjs | 1220 | returning command_id, action, target_chat_id, status, delivered_at, acked_at |
| stale | apps/watcher-api/src/server.mjs | 1236 | // FAIL_STALE_LOCAL_CAPABILITY_20260608_START |
| stale | apps/watcher-api/src/server.mjs | 1258 | // RECOVER_STALE_INTERCHAT_DELIVERIES_20260608_START |
| stale | apps/watcher-api/src/server.mjs | 1259 | async function recoverStaleInterChatDeliveries(body = {}) { |
| delivered | apps/watcher-api/src/server.mjs | 1276 | status, delivery_attempts, created_at, delivered_at, acked_at, last_error |
| delivered | apps/watcher-api/src/server.mjs | 1281 | and delivered_at is not null |
| delivered | apps/watcher-api/src/server.mjs | 1282 | and delivered_at < now() - ($1::int * interval '1 minute') |
| delivered | apps/watcher-api/src/server.mjs | 1283 | order by delivered_at asc |
| failed | apps/watcher-api/src/server.mjs | 1306 | when delivery_attempts >= $3 then 'failed' |
| queued | apps/watcher-api/src/server.mjs | 1307 | else 'queued' |
| delivered | apps/watcher-api/src/server.mjs | 1309 | delivered_at = case |
| delivered | apps/watcher-api/src/server.mjs | 1310 | when delivery_attempts >= $3 then delivered_at |
| acked | apps/watcher-api/src/server.mjs | 1313 | acked_at = case |
| acked | apps/watcher-api/src/server.mjs | 1314 | when delivery_attempts >= $3 then coalesce(acked_at, now()) |
| failed | apps/watcher-api/src/server.mjs | 1319 | then concat_ws('; ', nullif(last_error, ''), 'stale_interchat_delivery_failed_after_max_attempts') |
| queued | apps/watcher-api/src/server.mjs | 1320 | else concat_ws('; ', nullif(last_error, ''), 'stale_interchat_delivery_requeued') |
| delivered | apps/watcher-api/src/server.mjs | 1328 | and delivered_at is not null |
| delivered | apps/watcher-api/src/server.mjs | 1329 | and delivered_at < now() - ($1::int * interval '1 minute') |
| delivered | apps/watcher-api/src/server.mjs | 1330 | order by delivered_at asc |
| delivered | apps/watcher-api/src/server.mjs | 1334 | status, delivery_attempts, created_at, delivered_at, acked_at, last_error |
| queued | apps/watcher-api/src/server.mjs | 1342 | row.status === "queued" ? "REQUEUED_STALE_INTERCHAT_DELIVERY" : "FAILED_STALE_INTERCHAT_DELIVERY", |
| queued | apps/watcher-api/src/server.mjs | 1345 | message: row.status === "queued" |
| queued | apps/watcher-api/src/server.mjs | 1346 | ? "stale inter-chat delivery requeued" |
| failed | apps/watcher-api/src/server.mjs | 1347 | : "stale inter-chat delivery failed after max attempts", |
| stale | apps/watcher-api/src/server.mjs | 1369 | // RECOVER_STALE_INTERCHAT_DELIVERIES_20260608_END |
| stale | apps/watcher-api/src/server.mjs | 1371 | async function failStaleUnexecutedLocalCapability(body = {}) { |
| stale | apps/watcher-api/src/server.mjs | 1381 | // FAIL_STALE_SEND_FEEDBACK_OPTION_20260608 |
| delivered | apps/watcher-api/src/server.mjs | 1394 | c.delivered_at, |
| acked | apps/watcher-api/src/server.mjs | 1395 | c.acked_at |
| delivered | apps/watcher-api/src/server.mjs | 1399 | and c.delivered_at is not null |
| delivered | apps/watcher-api/src/server.mjs | 1400 | and c.delivered_at < now() - ($1::int * interval '1 minute') |
| failed | apps/watcher-api/src/server.mjs | 1405 | and e.event_type in ('RUN_COMMAND_OK','RUN_COMMAND_FAILED') |
| delivered | apps/watcher-api/src/server.mjs | 1407 | order by c.delivered_at asc |
| failed | apps/watcher-api/src/server.mjs | 1441 | set status = 'failed', |
| acked | apps/watcher-api/src/server.mjs | 1442 | acked_at = coalesce(acked_at, now()), |
| delivered | apps/watcher-api/src/server.mjs | 1452 | delivered_at, |
| acked | apps/watcher-api/src/server.mjs | 1453 | acked_at |
| failed | apps/watcher-api/src/server.mjs | 1459 | await insertBridgeCommandEvent(row.command_id, "FAILED", { |
| failed | apps/watcher-api/src/server.mjs | 1463 | status: "failed", |
| delivered | apps/watcher-api/src/server.mjs | 1467 | delivered_at: row.delivered_at \|\| null, |
| acked | apps/watcher-api/src/server.mjs | 1468 | acked_at: row.acked_at \|\| null |
| stale | apps/watcher-api/src/server.mjs | 1486 | // FAIL_STALE_LOCAL_CAPABILITY_20260608_END |
| acked | apps/watcher-api/src/server.mjs | 1489 | // AUDIT_ACKED_UNEXECUTED_LOCAL_CAPABILITY_20260608_START |
| acked | apps/watcher-api/src/server.mjs | 1490 | async function auditAckedUnexecutedLocalCapability(body = {}) { |
| delivered | apps/watcher-api/src/server.mjs | 1510 | c.delivered_at, |
| acked | apps/watcher-api/src/server.mjs | 1511 | c.acked_at, |
| acked | apps/watcher-api/src/server.mjs | 1516 | where c.status = 'acked' |
| failed | apps/watcher-api/src/server.mjs | 1524 | and e.event_type in ('RUN_COMMAND_OK','RUN_COMMAND_FAILED') |
| acked | apps/watcher-api/src/server.mjs | 1526 | order by c.acked_at desc |
| failed | apps/watcher-api/src/server.mjs | 1558 | set status = 'failed', |
| acked | apps/watcher-api/src/server.mjs | 1559 | acked_at = coalesce(acked_at, now()), |
| acked | apps/watcher-api/src/server.mjs | 1560 | last_error = concat_ws('; ', nullif(last_error, ''), 'acked_without_local_execution') |
| delivered | apps/watcher-api/src/server.mjs | 1570 | delivered_at, |
| acked | apps/watcher-api/src/server.mjs | 1571 | acked_at, |
| failed | apps/watcher-api/src/server.mjs | 1580 | await insertBridgeCommandEvent(row.command_id, "FAILED", { |
| failed | apps/watcher-api/src/server.mjs | 1584 | status: "failed", |
| acked | apps/watcher-api/src/server.mjs | 1585 | message: "command was acked without local execution", |
| acked | apps/watcher-api/src/server.mjs | 1587 | error: "acked_without_local_execution", |
| delivered | apps/watcher-api/src/server.mjs | 1588 | delivered_at: row.delivered_at \|\| null, |
| acked | apps/watcher-api/src/server.mjs | 1589 | acked_at: row.acked_at \|\| null, |
| acked | apps/watcher-api/src/server.mjs | 1596 | await enqueueBridgeCommandFailureFeedback(row, "acked_without_local_execution"); |
| acked | apps/watcher-api/src/server.mjs | 1608 | // AUDIT_ACKED_UNEXECUTED_LOCAL_CAPABILITY_20260608_END |
| acked | apps/watcher-api/src/server.mjs | 1614 | const status = String(body.status \|\| "acked").trim(); |
| acked | apps/watcher-api/src/server.mjs | 1619 | const finalStatus = status === "failed" ? "failed" : "acked"; |
| acked | apps/watcher-api/src/server.mjs | 1621 | if (finalStatus === "acked") { |
| failed | apps/watcher-api/src/server.mjs | 1630 | and e.event_type in ('RUN_COMMAND_OK','RUN_COMMAND_FAILED') |
| failed | apps/watcher-api/src/server.mjs | 1656 | await insertBridgeCommandEvent(commandId, finalStatus === "failed" ? "RUN_COMMAND_FAILED" : "RUN_COMMAND_OK", { |
| completed | apps/watcher-api/src/server.mjs | 1661 | message: "local capability execution completed before ack", |
| acked | apps/watcher-api/src/server.mjs | 1681 | acked_at = now(), |
| acked | apps/watcher-api/src/server.mjs | 1684 | returning id, command_id, status, acked_at |
| acked | apps/watcher-api/src/server.mjs | 1698 | finalStatus === "failed" ? "FAILED" : "ACKED", |
| failed | apps/watcher-api/src/server.mjs | 1700 | finalStatus === "failed" ? (error \|\| "command failed") : "command acknowledged", |
| failed | apps/watcher-api/src/server.mjs | 1702 | stage: finalStatus === "failed" ? "FAILED" : "DONE", |
| delivered | apps/watcher-api/src/server.mjs | 1762 | ["delivered_message"], |
| failed | apps/watcher-api/src/server.mjs | 2003 | database: { ok: false, reason: "database_check_failed" }, |
| queued | apps/watcher-api/src/server.mjs | 2212 | if (req.method === "POST" && url.pathname === "/bridge/commands/cancel-stale-queued") { |
| ... | ... | ... | ... |
| truncated | showing 120 of 232 rows | | |

## Dangerous capability evidence

The following references are evidence for risk classification only, not approval to expose these capabilities in WS AI Office.

| term | file | line | evidence |
|---|---|---|---|
| git-op | apps/watcher-api/src/server.mjs | 2 | import { createHash } from "node:crypto"; import { Pool } from "pg"; import { handleGitOp } from "./git-op.mjs"; import { handleCodexAnalyze } from "./codex-analyze.mjs"; import... |
| git-op | apps/watcher-api/src/server.mjs | 11 | // GIT_OP_CLOUD_ACTION_V2 - imported from ./git-op.mjs |
| git-op | apps/watcher-api/src/server.mjs | 2346 | if (req.method === "POST" && url.pathname === "/git-op") { |
| codex-analyze | apps/watcher-api/src/server.mjs | 2363 | if (req.method === "POST" && url.pathname === "/codex-analyze") { |
| db-query | apps/watcher-api/src/server.mjs | 2379 | if (req.method === "POST" && url.pathname === "/db-query") { |
| file-ops | apps/watcher-api/src/server.mjs | 2396 | if (req.method === "POST" && url.pathname === "/file-ops") { |
| cleanup | apps/watcher-api/src/server.mjs | 2413 | if (req.method === 'POST' && url.pathname === '/cleanup') { |
| cleanup | apps/watcher-api/src/server.mjs | 2415 | const result = await handleCleanup(pool); |
| cleanup | apps/watcher-api/src/server.mjs | 2416 | writeJson(res, 200, { ok: true, service: SERVICE_NAME, cleanup: result, timestamp: nowIso() }); |
| cleanup | apps/watcher-api/src/message-queue.mjs | 162 | // Run auto-cleanup |
| cleanup | apps/watcher-api/src/message-queue.mjs | 163 | export async function runCleanup() { |
| cleanup | apps/watcher-api/src/message-queue.mjs | 167 | await queuePool.query("SELECT ops.cleanup_stale_messages()"); |
| cleanup | apps/watcher-api/src/broker.mjs | 140 | // Cleanup stale claims first |
| cleanup | apps/watcher-api/src/broker.mjs | 141 | await client.query("SELECT ops.cleanup_stale_messages()"); |
| git-op | extension-next/content_script.js | 1110 | var CLOUD_ACTIONS = ["git-op", "codex-analyze", "db-query", "file-ops", "read-file-ref", "read-file-slice", "write-text-file", "create-file"]; |
| git-op | extension-next/capability_router.js | 17 | "git-op", |
| codex-analyze | extension-next/capability_router.js | 18 | "codex-analyze", |
| db-query | extension-next/capability_router.js | 19 | "db-query" |
| git-op | extension-next/capability_router.js | 36 | "git-op": "/git-op", |
| codex-analyze | extension-next/capability_router.js | 37 | "codex-analyze": "/codex-analyze", |
| db-query | extension-next/capability_router.js | 38 | "db-query": "/db-query" |

## Phase B decision

Evidence extraction is complete for contract-study purposes.

No runtime gateway integration is approved by this document.

## Next recommended micro

Create a WS AI Office internal gateway contract schema draft based on this evidence, still documentation only.
