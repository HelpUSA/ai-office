# AI Office + Pizza App - Cross-Repo Smoke Coordination

Date: 2026-07-08
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

## Purpose

This Micro56 update tightens cross-repo smoke coordination between AI Office and Pizza App after Pizza App Micro55 normalized the readonly approval gate. The cross-repo smoke now validates the Pizza App approval gate by explicit markers instead of treating it as a legacy existence-only artifact.

## AI Office expected artifacts

- cross-repo readiness summary
- approval gate manifest
- fixture schema contract
- synthetic fixture plan
- synthetic fixture
- cross-repo smoke coordination
- security and authorization matrix
- snapshot consumption plan
- snapshot fixture validation plan
- readonly contract alignment

## Pizza App expected artifacts

- readonly snapshot design
- readonly route staging plan
- readonly approval gate
- readonly runtime guard
- docs suite smoke

## Strict Pizza approval gate marker validation

The Pizza App approval gate must now include approval_state, not_approved, runtime_implementation_allowed, runtime_implementation_allowed: False, readonly_snapshot_consumption_allowed, production_route_allowed, live_production_data_access_allowed, gateway_runtime_integration_allowed, database_change_allowed, migration_allowed, approved readonly snapshots, schema_version, snapshot_id, source_commit, generated_at, snapshot timestamp, checksum, staleness policy, pagination policy, timeout policy, tenant isolation, store isolation, audit trail, rollback and disable strategy, disable switch, least privilege, deny by default, and safe failure.

## Safe failure

Missing Pizza App docs are safe failure. Missing AI Office docs are safe failure. Missing synthetic fixture is safe failure. Unknown schema_version is safe failure. Missing source_commit is safe failure. Failed checksum validation is safe failure. Stale snapshot is safe failure. Missing tenant isolation is safe failure. Missing store isolation is safe failure. Missing audit trail is safe failure. Missing approval_state is safe failure. Missing runtime_implementation_allowed is safe failure.

## Runtime boundary

The cross-repo smoke must not create routes, change databases, run migrations, start runtime gateway integration, access live production data, poll production queues, send customer messages, mutate orders, mutate menus, capture payments, refund payments, or change delivery status.

## Validation summary

Pizza App remains the source of truth. AI Office consumes approved readonly snapshots only. Runtime remains disabled by default and blocked until manual approval gate completion. The normalized Pizza approval gate allows the AI Office cross-repo smoke to enforce the same gate markers from the consumer side.
