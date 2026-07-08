# AI Office + Pizza App - Security and Authorization Matrix

Date: 2026-06-18
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

This Micro47 document defines security and authorization gates for AI Office consuming Pizza App approved readonly snapshots. Pizza App remains the source of truth. AI Office treats snapshots as advisory context only.

## Authorization matrix

- snapshot producer: Pizza App readonly export process, disabled by default.
- snapshot consumer: AI Office readonly reader, readonly only.
- operator approver: human approval for first integration step and any enable switch.
- auditor: reviews snapshot_id, schema_version, source_commit, tenant isolation, store isolation, checksum, staleness, pagination, timeout, authorization_status, and rejected_reason.
- administrator: may disable consumption but must not bypass validation gates.

## Tenant and store isolation

tenant isolation and store isolation are mandatory. A snapshot scoped to one tenant_id or store_id must never be visible to another tenant or store. Unknown tenant scope is safe failure. Unknown store scope is safe failure.

## Least privilege

AI Office receives only the fields needed for recommendation context. No customer secrets, no payment tokens, no private credentials, no production queue access, and no write access are allowed.

## Required validation gates

- approved readonly snapshots only.
- schema_version known and approved.
- source_commit recorded.
- snapshot timestamp present.
- checksum validated.
- staleness checked before use.
- tenant isolation verified.
- store isolation verified.
- pagination and result-size limits enforced.
- timeout behavior documented.
- audit trail recorded.
- rollback and disable strategy available.

## Deny by default

Missing snapshots are safe failure. Stale snapshots are safe failure. Unknown schema_version is safe failure. Failed checksum validation is safe failure. Missing authorization is safe failure. Ambiguous tenant or store scope is safe failure.

## Forbidden behavior in this phase

No route creation. No database change. No migration. No runtime gateway integration. No live polling. No production database access. No customer messages. No order mutation. No menu mutation. No payment capture. No refund.

## Audit trail

Every snapshot consumption decision must record consumer name, snapshot_id, schema_version, source_commit, snapshot timestamp, tenant_id or store_id scope, validation_status, authorization_status, staleness status, rejected_reason, and recommendation id when used.

## Rollback and disable strategy

Snapshot consumption remains disabled by default. A disable switch must stop AI Office consumption without changing Pizza App operations.

## Expected next steps

Micro48 in Pizza App covers staging for a future readonly route. Micro49 in AI Office covers snapshot fixture validation. A cross-repo readiness summary should confirm Micro45 through Micro49 are docs-only, smoke-covered, pushed, and blocked from runtime integration until approval gates are satisfied.
