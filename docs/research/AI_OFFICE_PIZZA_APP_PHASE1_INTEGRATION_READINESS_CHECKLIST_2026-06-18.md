'# AI Office + Pizza App - Phase 1 Integration Readiness Checklist

Date: 2026-06-18
Status: documentation only. No runtime gateway integration.

## Purpose

This Phase 1 Integration Readiness Checklist defines what must be true before any future Pizza App and AI Office integration. Phase 1 is readonly only. It prepares safe operational visibility without writes, execution, payment actions, campaign sending, database mutation, direct production queue reads or local runner access.

## Phase 1 principle

Pizza App remains the source of truth. AI Office may only read approved operational snapshots through explicitly designed readonly surfaces. AI Office must not mutate Pizza App state.

## Required Pizza App readiness

### Readonly endpoint contract

Conceptual readonly surfaces:

- GET /ai-office/readonly/orders/summary
- GET /ai-office/readonly/orders/recent
- GET /ai-office/readonly/orders/delayed
- GET /ai-office/readonly/menu/summary
- GET /ai-office/readonly/customers/summary
- GET /ai-office/readonly/finance/daily-summary

Authentication and authorization must be defined before any real endpoint is exposed. Data minimization must be defined before any real integration. Snapshot behavior remains preferred over live production queue reads. Auditability, Rate limits and safety limits, and Test environment first are required.

## Required AI Office readiness

- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- no runtime gateway integration
- no live polling
- no real claim
- no real ack
- ACK posting remains disabled
- no production queue read
- no direct database query by AI Office
- no command execution from app runtime
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no db-query
- no file-ops
- no codex-analyze

## Forbidden Phase 1 actions

- no mutation of orders
- no delivery status change
- no payment capture
- no refund
- no coupon creation
- no campaign sending
- no menu price change
- no menu availability change
- no customer message sending
- no customer data export
- no stock mutation
- no supplier order creation

## Phase 1 smoke expectations

- readonly API contract draft
- suggestion contract draft
- commercial plan matrix
- Phase 1 Integration Readiness Checklist
- commercial research only
- documentation only

## Handoff to Pizza App repository

The next safe cross-repository activity is a Pizza App repository readonly discovery and docs-only preparation pass.

## Recommended next safe micro

Next: Pizza App repository readonly discovery.
