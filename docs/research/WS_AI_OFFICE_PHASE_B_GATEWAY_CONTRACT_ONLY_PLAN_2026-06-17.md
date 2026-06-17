# WS AI Office Phase B Gateway Contract-Only Plan

Status: planning document only. No mutation and no execution.

## Current baseline

Phase A readonly compatibility is implemented and remotely validated on Railway.

Validated commit:

    f8470d4 feat: add phase a readonly compatibility routes

Validation recorded in:

- docs/research/WS_AI_OFFICE_PHASE_A_REMOTE_VALIDATION_2026-06-17.md
- docs/obsidian/Decisions/Phase_A_Readonly_Remote_Validation.md

Current safety state:

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- gateway_mode=not_configured

## Purpose of Phase B

Study the AI Bridge gateway contract without enabling any live gateway operation.

Phase B should classify envelope fields, response fields, statuses and safety rules for:

| Method | Route | Purpose | Phase B action | Runtime enabled? |
|---|---|---|---|---|
| GET | /bridge/next-action | gateway polling / next action contract | study only | no |
| POST | /bridge/events | gateway event callback contract | study only | no |
| POST | /bridge/acks | delivery ACK contract | study only | no |
| GET | /claim | broker claim contract | study only | no |
| POST | /ack | broker ACK contract | study only | no |

## Explicit non-goals

Phase B must not:

- create commands
- enqueue messages
- poll a live queue
- claim work
- ACK work
- post events to AI Bridge
- write to database
- execute local commands
- call git, file-ops, db-query or codex-analyze
- add credentials or secrets

## Required outputs

Phase B should produce documentation only:

1. Gateway contract evidence table.
2. Envelope fields table.
3. Status lifecycle table.
4. Risk and blocking rules.
5. Readonly smoke design for future Phase C.

## Contract fields to extract

### Command identity

- command_id
- id
- conversation_id
- source_chat_id
- target_chat_id
- destino
- origem

### Delivery semantics

- status
- queued
- delivered
- acked
- failed
- result_is_final
- no_reply
- attempts
- last_error

### Action semantics

- action
- type
- delivery_kind
- run-command
- send-chat-message
- payload
- command
- cwd
- timeout_seconds

### Event semantics

- event_type
- message_kind
- chat_id
- text
- result
- error
- created_at

## Safety policy for future implementation

Any future Phase C adapter must:

- default to disabled
- require explicit env flag
- expose dry-run mode first
- reject execution_dangerous categories by default
- reject debug_admin categories by default
- log every rejected action
- keep database_enabled=false unless a DB migration is approved
- keep local_runner_enabled=false unless a local runner micro is approved

## Planned evidence sources

Readonly source files to inspect in ai-bridge:

- D:/dev/autocode/ai-bridge/apps/watcher-api/src/server.mjs
- D:/dev/autocode/ai-bridge/extension-next/background.js
- D:/dev/autocode/ai-bridge/extension-next/content_script.js
- D:/dev/autocode/ai-bridge/extension-next/capability_router.js
- D:/dev/autocode/ai-bridge/apps/watcher-api/src/message-queue.mjs
- D:/dev/autocode/ai-bridge/apps/watcher-api/src/broker.mjs

## Phase B step sequence

### Micro 24B

Commit this plan.

### Micro 25A

Readonly extract contract evidence from AI Bridge source files into reports and docs.

### Micro 25B

Commit contract evidence docs.

### Micro 26A

Create a WS AI Office internal contract schema draft, still documentation only.

## Decision

Proceed to Phase B only as contract study.

No runtime gateway integration is approved yet.
