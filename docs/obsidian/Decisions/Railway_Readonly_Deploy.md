# Railway Readonly Deploy

## Decision

WS AI Office has a readonly Railway deployment.

URL:

    https://web-production-de25.up.railway.app

## Validated endpoints

- GET /health
- GET /ready
- GET /status
- GET /agents
- GET /tasks
- GET /audit-events

## Safety flags

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false

## Remote smoke

    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_remote_readonly.ps1
