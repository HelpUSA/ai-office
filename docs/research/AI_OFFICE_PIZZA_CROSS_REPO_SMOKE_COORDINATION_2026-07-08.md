# AI Office + Pizza App - Cross-Repo Smoke Coordination

Date: 2026-07-08
Status: documentation only. No route creation. No database change. No migration. No runtime gateway integration. No live production data access.

## Purpose

This Micro54 document defines cross-repo smoke coordination between AI Office and Pizza App for readonly snapshot planning.

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

## Per-file marker policy

The cross-repo smoke must not assume every Pizza App document uses identical language. Snapshot design and route staging plan carry the full docs-only runtime boundary, including No live production data access. The Pizza approval gate is treated as a legacy gate artifact and is existence-validated in this AI Office smoke. A future Pizza-side normalization micro may add stronger markers there.

## Safe failure

Missing Pizza App docs are safe failure. Missing AI Office docs are safe failure. Missing synthetic fixture is safe failure. Unknown schema_version is safe failure. Missing source_commit is safe failure. Failed checksum validation is safe failure. Stale snapshot is safe failure. Missing tenant isolation is safe failure. Missing store isolation is safe failure. Missing audit trail is safe failure.

## Runtime boundary

The cross-repo smoke must not create routes, change databases, run migrations, start runtime gateway integration, access live production data, poll production queues, send customer messages, mutate orders, mutate menus, capture payments, refund payments, or change delivery status.

## Validation summary

Pizza App remains the source of truth. AI Office consumes approved readonly snapshots only. Runtime remains disabled by default and blocked until manual approval gate completion.
