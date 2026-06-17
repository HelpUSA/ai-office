# WS AI Office - Phase C Readiness Guardrails Checklist

Date: 2026-06-17
Status: documentation only. No runtime gateway integration.

## Purpose

Define the required checklist before any future Phase C implementation. This is a readiness and guardrails document only. It does not enable live gateway behavior, polling, claim, ack, queue mutation, database writes, local execution or production integration.

## Current protected baseline

- Phase A readonly compatibility routes are already documented and validated.
- Phase B gateway contract-only documents exist.
- Phase C readonly smoke design exists.
- scripts/smoke_phase_c_readonly_design_docs.py protects the Phase C design markers.
- Current safety flags remain database_enabled=false, execution_enabled=false, local_runner_enabled=false and gateway_integration_enabled=false.

## Required green checks before future implementation

- Repo status must be clean.
- Existing docs-only smokes must pass.
- Any new code must be preceded by a docs-only plan.
- Any route or endpoint work must remain readonly unless explicitly approved later.
- Any implementation must include a smoke before commit.
- Any push must be followed by final readonly verification.

## Hard blockers

Stop if the task requires credentials, secrets, live gateway polling, queue mutation, database access, command execution, claim posting, ack posting, event posting, production queue read, file-ops beyond explicit reviewed paths, db-query or codex-analyze.

## Safety markers

- documentation only
- readiness checklist
- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- no runtime gateway integration
- no live polling
- no real claim
- no real ack
- ACK posting remains disabled

## Runtime behaviors still forbidden

- no GET /bridge/next-action call
- no POST /bridge/events call
- no POST /bridge/acks call
- no GET /claim call
- no POST /ack call
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no db-query
- no file-ops
- no codex-analyze
- no production queue read

## Future safe sequence

1. Keep Phase C implementation disabled by default.
2. Add readonly-only code behind explicit disabled flags.
3. Add local static smoke first.
4. Add route smoke only if it does not call live gateway.
5. Validate with py_compile, targeted smokes and git diff --check.
6. Commit small, push, and run final readonly verification.

## Next safe micro

Create a docs-only smoke to protect this checklist before considering any future Phase C implementation step.
