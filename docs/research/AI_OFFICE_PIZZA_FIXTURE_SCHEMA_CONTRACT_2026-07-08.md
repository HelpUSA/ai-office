# AI Office + Pizza App - Fixture Schema Contract

Date: 2026-07-08
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

## Purpose

This Fixture Schema Contract artifact keeps the Pizza App readonly snapshot work in a docs-only and smoke-only phase. Pizza App remains the source of truth. AI Office consumes approved readonly snapshots only after explicit manual approval gate completion.

## Required markers and gates

- documentation only
- No route creation
- No database change
- No migration
- No runtime gateway integration
- No live production data access
- Pizza App remains the source of truth
- approved readonly snapshots
- schema_version
- snapshot_id
- source_commit
- generated_at
- snapshot timestamp
- checksum
- staleness policy
- pagination policy
- timeout policy
- tenant isolation
- store isolation
- audit trail
- rollback and disable strategy
- safe failure
- manual approval gate
- Micro52
- source_repository
- source_branch
- source_commit
- tenant_id
- store_id
- record_count
- records
- data minimization
- max_age_seconds
- timeout_ms

## Boundary

This artifact authorizes only documentation, synthetic fixtures, and smoke tests. It does not authorize production routes, runtime gateway integration, live data access, database changes, migrations, order mutation, menu mutation, payment capture, refund, delivery mutation, or production queue access.
