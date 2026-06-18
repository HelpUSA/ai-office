# AI Office + Pizza App - Readonly Contract Alignment

Date: 2026-06-18
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration.

## Purpose

This AI Office-side alignment records how AI Office documentation aligns with the Pizza App readonly API contract draft and readonly implementation checklist.

## Pizza App source documents

- Micro40 readonly discovery: docs/research/AI_OFFICE_PIZZA_APP_READONLY_DISCOVERY_2026-06-18.md
- Micro41 readonly API contract draft: docs/research/AI_OFFICE_PIZZA_APP_READONLY_API_CONTRACT_DRAFT_2026-06-18.md
- Micro42 readonly implementation checklist: docs/research/AI_OFFICE_PIZZA_READONLY_IMPLEMENTATION_CHECKLIST_2026-06-18.md

Known Pizza App commits:

- 37ac4c5 docs: add ai office readonly discovery
- 6dee140 docs: draft ai office readonly api contract
- 05b8920 docs: add readonly implementation checklist

## Alignment principles

1. Pizza App remains the source of truth.
2. AI Office consumes only approved readonly snapshots in future phases.
3. Missing or stale snapshots are treated as safe failure, not permission to query live data.
4. AI Office does not create, alter, cancel, refund, message, deliver, or mutate anything in Pizza App.
5. AI Office suggestions remain advisory until explicit approval gates exist.
6. AI Office must keep traceability to Pizza App contract and checklist versions.

## AI Office documentation requirements

Before any future implementation phase, AI Office must document:

- snapshot consumption plan
- snapshot schema expectations
- tenant and store isolation assumptions
- data minimization rules
- audit and traceability rules
- stale snapshot behavior
- error and timeout behavior
- result-size and pagination expectations
- approval gates for leaving docs-only
- rollback and disable strategy

## Safety boundary

Forbidden in this phase:

- creating real Pizza App routes
- changing database schema
- running migrations
- direct production database queries
- reading production queues
- live polling
- payment capture
- refund
- coupon creation
- campaign sending
- menu mutation
- customer message sending
- order mutation
- delivery status change
- stock or supplier mutation
- runtime gateway integration
- local runner access from app runtime

## Expected next micros

1. Micro44 in Pizza App: consolidate docs smokes for discovery, contract, and checklist.
2. Micro45 in AI Office: draft snapshot consumption plan, docs-only.
3. Micro46 in Pizza App: draft readonly snapshot design, docs-only.
4. Micro47 in AI Office: draft security and authorization matrix, docs-only.
5. Micro48 in Pizza App: draft staging plan for future readonly route, docs-only.

## Validation checklist

This alignment is valid only if:

- AI Office docs reference Pizza App contract and checklist names.
- AI Office records Pizza App as the source of truth.
- AI Office blocks route creation, DB changes, migrations, and runtime gateway integration.
- AI Office records the future handoff to snapshot consumption planning.
