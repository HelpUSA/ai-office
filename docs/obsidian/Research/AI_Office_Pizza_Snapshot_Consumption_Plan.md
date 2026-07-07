# AI Office + Pizza App - Snapshot Consumption Plan

Date: 2026-06-18
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

Pizza App remains the source of truth. AI Office consumes approved readonly snapshots only.

Snapshot handoff must include snapshot_id, schema_version, source_commit, snapshot timestamp, store_id or tenant_id scope, checksum, staleness, audit, pagination, and timeout.

Rules: Missing snapshots are safe failure. Stale snapshots are safe failure. Unknown schema_version is safe failure. Failed checksum validation is safe failure. tenant isolation is required.

Approval gates: Pizza App readonly snapshot design approved; AI Office snapshot schema approved; fixture tests approved; manual approval before runtime use.

Rollback and disable strategy: disabled by default; disable switch stops consumption without affecting Pizza App operations.

Forbidden behavior in this phase: no live polling, no production database access, no customer messages, no order mutation, no payment capture, no refund.

Expected next micros: Micro46 in Pizza App, Micro47 in AI Office, Micro48 in Pizza App, Micro49 in AI Office.
