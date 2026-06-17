# WS AI Office - Deployment

Status: Railway-ready local foundation.

## Current scope

The current HTTP API is readonly.

Exposed endpoints:

- GET /health
- GET /ready
- GET /status
- GET /agents
- GET /tasks
- GET /audit-events

The current API does not:

- connect to a real database
- execute local commands
- send commands to AI Bridge Local
- process approvals
- mutate production data

## Railway process

The repository includes:

- Procfile
- requirements.txt
- src/ai_office/http_api.py

Expected Railway process:

    web: python -m ai_office.http_api

## Environment variables

Required or supported variables:

    PORT=<provided by Railway>
    HOST=0.0.0.0
    PYTHONPATH=src

## Local smoke example

PowerShell:

    $env:PYTHONPATH = "D:\dev\autocode\ai-office\src"
    $env:HOST = "127.0.0.1"
    $env:PORT = "8787"
    python -m ai_office.http_api

Then check:

    http://127.0.0.1:8787/health
    http://127.0.0.1:8787/ready
    http://127.0.0.1:8787/status

## Safety gates before real deploy

Before any deploy, verify:

- all local smokes pass
- GET /ready reports database_enabled=false
- GET /ready reports execution_enabled=false
- GET /ready reports local_runner_enabled=false
- no secrets are committed
- no .env file is committed
- no local runtime database is committed
- no local logs are committed

## Future phases

Phase 1: readonly cloud deploy.
Phase 2: Postgres integration with explicit approval.
Phase 3: approval gate.
Phase 4: readonly local runner bridge.
Phase 5: controlled execution with audit, rollback plan and smoke requirements.

## Validated Railway deployment

Readonly deployment URL:

    https://web-production-de25.up.railway.app

Validation status:

- /health OK
- /ready OK
- /status OK
- /agents OK
- /tasks OK
- /audit-events OK

Validated safety flags:

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false

Remote smoke command:

    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_remote_readonly.ps1
