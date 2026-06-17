# WS AI Office - Watcher Usage Lessons

Date: 2026-06-17
Scope: Micro28A and Micro28B operational lessons.
Mode: documentation only.

## Purpose

This note records practical watcher usage lessons discovered while running readonly and docs-first work for WS AI Office. It is not a runtime gateway integration plan and does not approve production execution.

## Micro28A lessons

- For run-command execution, use target_chat_id=gateway-brain-supervisor.
- For run-command execution, use delivery_kind=local_capability.
- payload.cwd must point to the repository root.
- payload.timeout_seconds should be explicit.
- payload.command worked reliably for readonly inspection.
- Do not use the destination chat id as the command execution target.

## Micro28B lessons

- Cross-chat reports use action=send-chat-message and type=send-chat-message.
- Cross-chat reports use delivery_kind=inter_agent_message.
- Cross-chat reports must keep message as a top-level field, not inside payload.
- Keep cross-chat messages short and in STEP; STATUS; FILES; VALIDATION; RISKS; NEXT format.
- Avoid fragile inline PowerShell patterns such as pipeline variables that may be degraded during transport.
- Avoid command strings with nested quotes when a shorter payload.command can do the job.
- script_text/script_ext was unstable in this environment and should not be the first choice here.

## Safety boundary

These lessons do not enable runtime gateway integration. The following remain disabled or out of scope:
- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- no runtime gateway integration
- no real DB execution
- no local runner execution
- no real claim
- no real ack
- ACK posting remains disabled

## Recommended next micro

Keep the next step docs-first and smoke-first. A safe next micro is to reference this lesson note from a Phase B planning document or add a small docs-only smoke after Supervisor approval.
