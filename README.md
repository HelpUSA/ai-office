# WS AI Office

WS AI Office is a safe orchestration layer for agents, tasks, approvals, audit events, artifacts and controlled local execution.

Current status: readonly HTTP API foundation.

## Current capabilities

- readonly HTTP API
- in-memory service layer
- initial schema draft
- agent contracts
- task contracts
- command contracts
- local run result contracts
- Railway-ready process definition
- local smoke tests

## Current HTTP endpoints

- GET /health
- GET /ready
- GET /status
- GET /agents
- GET /tasks
- GET /audit-events

## Safety posture

The current version is intentionally readonly.

It does not:

- connect to a real database
- execute local commands
- call AI Bridge Local
- mutate production data
- run migrations
- deploy automatically

Readiness flags exposed by /ready:

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false

## Local run

PowerShell:

    $env:PYTHONPATH = "D:\dev\autocode\ai-office\src"
    $env:HOST = "127.0.0.1"
    $env:PORT = "8787"
    python -m ai_office.http_api

Then open:

    http://127.0.0.1:8787/health
    http://127.0.0.1:8787/ready
    http://127.0.0.1:8787/status

## Railway

The repository includes:

- Procfile
- requirements.txt
- docs/DEPLOYMENT.md

Expected process:

    web: python -m ai_office.http_api

Required environment:

    PYTHONPATH=src
    HOST=0.0.0.0
    PORT=<provided by Railway>

## Smokes

Run:

    $env:PYTHONPATH = "D:\dev\autocode\ai-office\src"
    python scripts\smoke_contracts.py
    python scripts\smoke_api_readonly.py
    python scripts\smoke_http_api.py
    python scripts\smoke_http_api_server.py
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_local_mode.ps1

Expected:

- SMOKE_CONTRACTS_OK
- SMOKE_API_READONLY_OK
- SMOKE_HTTP_API_OK
- SMOKE_HTTP_API_SERVER_OK
- SMOKE_RAILWAY_LOCAL_MODE_OK

## Architecture decisions

- AI Bridge web/API is the cloud/API reference.
- AI Bridge Local is the official local executor reference.
- WS AI Office is not a direct copy of either project.
- Railway/cloud orchestrates.
- Local runner executes only after explicit gates are implemented.

## Next phases

1. Deploy readonly API.
2. Add Postgres integration behind explicit approval.
3. Add approval gate.
4. Add readonly AI Bridge Local status integration.
5. Add controlled command execution with audit and rollback.

## Live readonly deployment

Current Railway readonly deployment:

    https://web-production-de25.up.railway.app

Validated endpoints:

- GET /health
- GET /ready
- GET /status
- GET /agents
- GET /tasks
- GET /audit-events

Validated safety flags:

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false

Remote smoke:

    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\smoke_railway_remote_readonly.ps1

## Local gateway correction

Architectural correction: WS AI Office will not use `D:\dev\autocode\ai-bridge-local` as the implementation base.

The local gateway reference to use is the one already present inside `D:\dev\autocode\ai-bridge`, because that gateway communicates with the Railway API.

The separate `ai-bridge-local` folder is not the official base for WS AI Office implementation.
