# WS AI Office Phase A Readonly Route Plan

Status: route plan only. No runtime integration yet.

## Purpose

Define the first safe readonly compatibility routes for WS AI Office after studying AI Bridge watcher-api.

## Current WS AI Office routes

| Method | Route | Status | Purpose |
|---|---|---|---|
| GET | /health | implemented | service health |
| GET | /ready | implemented | readiness and safety flags |
| GET | /status | implemented | service status and counts |
| GET | /agents | implemented | readonly agents list |
| GET | /tasks | implemented | readonly tasks list |
| GET | /audit-events | implemented | readonly audit events list |

## Phase A target routes

| Method | Route | Source inspiration | Safety | Purpose | Implementation note |
|---|---|---|---|---|---|
| GET | /storage-status | WS AI Office internal | readonly_safe | expose current storage mode | Return in_memory initially; Postgres false. |
| GET | /bridge/health | AI Bridge /bridge/health | readonly_safe | compatibility-style gateway health | Return WS AI Office gateway compatibility status, no polling. |
| GET | /gateway/status | WS AI Office internal | readonly_safe | summarize gateway integration status | Return disabled/not_configured initially. |
| GET | /compatibility/routes | WS AI Office internal | readonly_safe | list supported/planned compatibility routes | Static/read-only route plan response. |
| GET | /safety | WS AI Office internal | readonly_safe | expose safety flags and blocked categories | Show execution disabled, local runner disabled, DB disabled. |

## Explicitly excluded from Phase A

These routes must not be implemented yet:

- POST /bridge/commands
- GET /bridge/next-action
- POST /bridge/events
- POST /bridge/acks
- POST /enqueue
- GET /claim
- POST /ack
- POST /git-op
- POST /db-query
- POST /file-ops
- POST /codex-analyze
- POST /cleanup

## Reason for exclusion

Phase A is visibility only. It must not create commands, claim commands, acknowledge work, mutate queues, call local gateway, write DB state, or trigger execution.

## Expected Phase A behavior

- database_enabled remains false.
- execution_enabled remains false.
- local_runner_enabled remains false.
- gateway_integration_enabled remains false.
- compatibility_mode is documented only.
- every new route is GET-only.
- every new route returns deterministic JSON from in-memory/static config.

## Proposed response shapes

### GET /storage-status

    {
      "ok": true,
      "storage_mode": "in_memory",
      "database_enabled": false,
      "database_configured": false
    }

### GET /bridge/health

    {
      "ok": true,
      "service": "ws-ai-office",
      "bridge_compatibility": "planned",
      "gateway_integration_enabled": false,
      "execution_enabled": false
    }

### GET /gateway/status

    {
      "ok": true,
      "gateway_integration_enabled": false,
      "gateway_source": "ai-bridge",
      "gateway_mode": "not_configured",
      "can_poll": false,
      "can_ack": false,
      "can_execute": false
    }

### GET /compatibility/routes

    {
      "ok": true,
      "phase": "A_readonly",
      "implemented": [],
      "planned_readonly": ["/storage-status", "/bridge/health", "/gateway/status", "/compatibility/routes", "/safety"],
      "blocked": ["/bridge/commands", "/bridge/next-action", "/bridge/events", "/bridge/acks", "/git-op", "/db-query", "/file-ops"]
    }

### GET /safety

    {
      "ok": true,
      "database_enabled": false,
      "execution_enabled": false,
      "local_runner_enabled": false,
      "gateway_integration_enabled": false,
      "blocked_categories": ["controlled_mutation", "gateway_extension", "execution_dangerous", "debug_admin"]
    }

## Smokes required before commit when implemented

- scripts/smoke_contracts.py
- scripts/smoke_api_readonly.py
- scripts/smoke_http_api.py
- scripts/smoke_http_api_server.py
- scripts/smoke_railway_local_mode.ps1
- scripts/smoke_railway_remote_readonly.ps1
- new smoke for Phase A readonly routes

## Next implementation micro

Implement GET-only Phase A readonly routes in src/ai_office/http_api.py and add a smoke that validates all safety flags remain false.
