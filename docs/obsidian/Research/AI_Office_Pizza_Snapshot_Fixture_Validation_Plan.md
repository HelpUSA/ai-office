# AI Office + Pizza App - Snapshot Fixture Validation Plan

Date: 2026-06-18
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

This Micro49 document defines how AI Office should validate Pizza App approved readonly snapshot fixtures before any runtime consumption. Pizza App remains the source of truth. AI Office consumes approved readonly snapshots only after explicit approval gates.

## Fixture scope

Fixtures must be synthetic or explicitly approved readonly snapshots. No live production data access is allowed. No production database query is allowed. No production queue access is allowed. No customer messages, order mutation, menu mutation, payment capture, refund, or delivery status mutation is allowed.

## Required fixture metadata

Each fixture must include snapshot_id, schema_version, source_repository, source_branch, source_commit, generated_at, snapshot timestamp, store_id or tenant_id scope, extraction_window, record_count, checksum, staleness policy, pagination policy, timeout policy, data minimization notes, audit trail fields, and disabled_by_default flag.

## Validation checklist

- schema_version is known and approved.
- source_commit is present and traceable.
- generated_at is present and parseable.
- snapshot timestamp is present and within staleness policy.
- checksum is present and validates fixture integrity.
- tenant isolation is explicit and verified.
- store isolation is explicit and verified.
- pagination and result-size limits are documented.
- timeout behavior is documented.
- audit trail fields are present.
- data minimization excludes customer secrets, payment tokens, private credentials, production queue payloads, and unnecessary personal data.
- fixture format is stable enough for deterministic smoke tests.

## Safe failure rules

Missing fixtures are safe failure. Stale fixtures are safe failure. Unknown schema_version is safe failure. Missing source_commit is safe failure. Missing generated_at is safe failure. Missing snapshot timestamp is safe failure. Failed checksum validation is safe failure. Tenant mismatch is safe failure. Store mismatch is safe failure. Pagination overflow is safe failure. Timeout is safe failure. Missing authorization is safe failure.

## Smoke expectations

The fixture validation smoke must validate marker coverage, metadata expectations, safe failure language, tenant isolation, store isolation, checksum, staleness, pagination, timeout, and audit trail requirements without touching live production data.

## Approval gates

Future implementation requires approved Pizza App readonly snapshot design, approved AI Office security and authorization matrix, approved fixture schema, approved sample fixtures, passing fixture validation smoke, passing stale snapshot tests, passing tenant isolation tests, passing store isolation tests, rollback and disable strategy, and manual approval before runtime use.

## Rollback and disable strategy

Fixture validation and snapshot consumption remain disabled by default. A disable switch must stop fixture consumption without affecting Pizza App operations. Rollback must not require database migration rollback because this phase forbids database change and migration.

## Expected next step

After Micro49, the safe next step is a cross-repo readiness summary that confirms Micro45 through Micro49 are docs-only, smoke-covered, pushed, and still blocked from runtime integration until approval gates are satisfied.
