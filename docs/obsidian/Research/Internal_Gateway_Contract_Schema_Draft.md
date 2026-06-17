# WS AI Office Internal Gateway Contract Schema Draft

Status: documentation only. No runtime gateway integration.

## Source evidence

- docs/research/WS_AI_OFFICE_PHASE_B_GATEWAY_CONTRACT_EVIDENCE_2026-06-17.md
- docs/obsidian/Research/Phase_B_Gateway_Contract_Evidence.md

## Safety baseline

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- gateway_mode=not_configured

## Contract objects

### GatewayCommandCandidate

Fields: command_id, target_chat_id, source_chat_id, conversation_id, action, delivery_kind, payload, status, created_at.

Allowed status values for study: queued, delivered, acked, failed, stale.

### GatewayNextActionResponse

Fields: ok, action, command_id, target_chat_id, payload, no_reply, result_is_final.

Phase C rule: response is consumed only in dry-run until explicitly approved.

### GatewayAckRequest

Fields: command_id, status, runner_id, result, error, stdout_tail, stderr_tail, created_at.

Phase C rule: ACK posting remains disabled until explicit approval.

### GatewayEventRequest

Fields: chat_id, event_type, message_kind, text, payload, created_at.

Phase C rule: event posting remains disabled until explicit approval.

## Blocked capabilities

- git-op
- db-query
- file-ops
- codex-analyze
- cleanup
- run-command execution
- queue claim
- ACK mutation

## Decision

This schema is a documentation-only draft for future adapters. It does not approve runtime gateway integration.

## Next micro

Commit this schema draft, then create a readonly smoke/check script that verifies the docs exist and still state all runtime flags disabled.
