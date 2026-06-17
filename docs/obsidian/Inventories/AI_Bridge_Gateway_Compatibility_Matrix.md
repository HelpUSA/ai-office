# AI Bridge Gateway Compatibility Matrix

Status: initial compatibility matrix for WS AI Office.

## Purpose

This document classifies AI Bridge watcher-api routes by safety level before WS AI Office implements any compatibility layer.

Source evidence:

- docs/research/AI_BRIDGE_GATEWAY_CONTRACT_DRAFT_2026-06-17.md
- docs/research/AI_BRIDGE_WATCHER_API_ROUTES_2026-06-17.md

## Safety levels

- readonly_safe: can be studied or mirrored first because it does not create execution.
- controlled_mutation: changes state and needs validation, audit and later authorization.
- execution_dangerous: can trigger command/code/file/db/git execution or operational side effects.
- debug_admin: diagnostic/admin route, not for product surface by default.
- gateway_extension: route used by browser/local gateway, ACK, event, visibility or next-action flow.

## Compatibility matrix

| Method | Route | Category | Safety level | WS AI Office first action | Notes |
|---|---|---|---|---|---|
| GET | /health | service health | readonly_safe | mirror as health/readiness reference | Safe first integration target. |
| GET | /ready | service readiness | readonly_safe | mirror as readiness reference | Safe first integration target. |
| GET | /bridge/health | gateway health | readonly_safe | study and possibly add readonly compatibility endpoint | Useful for gateway status. |
| GET | /bridge/commands/timeline | command visibility | readonly_safe | study for future command audit view | Must not expose secrets. |
| GET | /bridge/ingest/status | ingest status | readonly_safe | study later | Readonly operational status. |
| GET | /queue-stats | queue visibility | readonly_safe | study later | Queue monitoring only. |
| GET | /broker-stats | broker visibility | readonly_safe | study later | Broker monitoring only. |
| GET | /api/brain/facts | brain/memory visibility | readonly_safe | defer until HelpUS AI audit | Could overlap with memory layer. |
| GET | /debug/db | diagnostics | debug_admin | do not expose publicly | Sensitive operational info. |
| GET | /debug/db-probe | diagnostics | debug_admin | do not expose publicly | Sensitive DB probe. |
| POST | /bridge/events | gateway event ingest | gateway_extension | study envelope only | Key route for extension/gateway events. |
| POST | /bridge/acks | delivery ACK | gateway_extension | study envelope only | Key route for delivery confirmation. |
| GET | /bridge/next-action | next action polling | gateway_extension | study polling contract | Important for local/browser gateway loop. |
| POST | /bridge/message-observations | passive observation | gateway_extension | study envelope only | Browser/content observation route. |
| POST | /bridge/visibility-resume | extension visibility | gateway_extension | study only | Browser lifecycle route. |
| POST | /bridge/command-candidates | candidate ingest | controlled_mutation | defer | Creates candidate command records. |
| POST | /bridge/ingest/promote | promotion | controlled_mutation | defer | Promotes ingest into state. |
| POST | /api/brain/ingest | brain ingest | controlled_mutation | defer until memory design | Writes/updates brain facts. |
| POST | /bridge/commands | command creation | controlled_mutation | defer until approval gates | Must not execute directly. |
| POST | /enqueue | queue mutation | controlled_mutation | defer | Adds message/command to queue. |
| GET | /claim | queue claim | gateway_extension | study only | Local/gateway pull endpoint. Could trigger work assignment. |
| POST | /ack | queue ACK | gateway_extension | study only | Broker acknowledgement. |
| POST | /ingest | ingest mutation | controlled_mutation | defer | Generic ingest mutation. |
| POST | /cleanup | operational mutation | debug_admin | do not implement initially | Can mutate/clean runtime state. |
| POST | /bridge/commands/cancel-stale-queued | operational mutation | debug_admin | do not implement initially | State repair route. |
| POST | /bridge/commands/audit-acked-unexecuted-local-capability | operational audit | debug_admin | do not implement initially | Repair/audit route. |
| POST | /bridge/commands/fail-stale-unexecuted-local-capability | operational mutation | debug_admin | do not implement initially | State repair route. |
| POST | /bridge/commands/recover-stale-interchat-deliveries | operational mutation | debug_admin | do not implement initially | State repair route. |
| POST | /bridge/commands/auto-ack-stale-delivered | operational mutation | debug_admin | do not implement initially | State repair route. |
| POST | /git-op | git operation | execution_dangerous | block until explicit approval gates | Can affect repositories. |
| POST | /codex-analyze | code analysis/execution-adjacent | execution_dangerous | block until explicit approval gates | Needs sandbox and audit policy. |
| POST | /db-query | database query | execution_dangerous | block until explicit approval gates | Can expose or mutate DB depending query. |
| POST | /file-ops | file operation | execution_dangerous | block until explicit approval gates | Can modify files. |

## Initial WS AI Office implementation order

### Phase A - readonly only

1. Add a local compatibility note only.
2. Add no runtime integration.
3. Later create optional readonly endpoints that mirror health/status concepts.

Candidate first endpoints to mirror or study:

- /health
- /ready
- /bridge/health
- /queue-stats
- /broker-stats

### Phase B - gateway contract study

Study only, do not implement execution:

- /bridge/next-action
- /bridge/events
- /bridge/acks
- /bridge/message-observations
- /claim
- /ack

### Phase C - controlled mutation

Only after Postgres, audit records and approval gates:

- /bridge/commands
- /enqueue
- /bridge/command-candidates
- /api/brain/ingest

### Phase D - dangerous/admin

Block by default:

- /git-op
- /db-query
- /file-ops
- /codex-analyze
- /cleanup
- stale recovery/admin routes

## Current decision

WS AI Office should not copy the AI Bridge server wholesale.

WS AI Office should first implement its own safer product model, then add compatibility endpoints or adapters only where needed.

## Next recommended micro

Create WS AI Office route plan for Phase A readonly compatibility only.
