# WS AI Office - Phase C Readonly Smoke Design

Date: 2026-06-17
Status: documentation only. No runtime gateway integration.

## Purpose

Define a future readonly smoke design for Phase C without enabling live gateway behavior. This document is a design note only and does not approve implementation of polling, claim, ack, event posting, database writes, local execution or production gateway integration.

## Baseline

- Phase A readonly compatibility routes were previously validated.
- Phase B contract-only evidence and schema docs exist.
- Watcher usage lessons are documented and protected by a docs-only smoke.
- Current safety flags remain database_enabled=false, execution_enabled=false, local_runner_enabled=false and gateway_integration_enabled=false.

## Future readonly smoke objective

A future Phase C smoke may verify local contract documentation and static safety invariants only. It must not call live gateway routes, mutate state, claim work, ack work, enqueue messages, post events or execute commands.

## Allowed checks

- Read local markdown docs from docs/research and docs/obsidian.
- Assert required contract field names exist in documentation.
- Assert disabled safety flags remain documented.
- Assert blocked route names are documented as study-only or disabled.
- Assert no runtime enablement text is introduced.

## Required readonly markers

- documentation only
- readonly smoke design
- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- no runtime gateway integration
- no live polling
- no real claim
- no real ack
- ACK posting remains disabled

## Blocked runtime behaviors

- no GET /bridge/next-action call
- no POST /bridge/events call
- no POST /bridge/acks call
- no GET /claim call
- no POST /ack call
- no run-command execution
- no send-chat-message execution
- no db-query
- no file-ops
- no codex-analyze
- no production queue read

## Candidate smoke structure

A future script may be named scripts/smoke_phase_c_readonly_design_docs.py. It should read this document plus the Phase B plan, contract schema draft and watcher usage lessons. It should fail if required readonly markers or disabled safety flags are missing.

## Stop conditions

Stop before code changes if a future step requires credentials, secrets, database access, live gateway polling, queue mutation, local command execution, claim or ack posting.

## Next safe micro

Create a docs-only smoke for this design after this document is reviewed and committed.
