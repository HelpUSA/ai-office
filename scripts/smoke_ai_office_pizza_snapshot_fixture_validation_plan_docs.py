from pathlib import Path
DOCS = [
    Path("docs/research/AI_OFFICE_PIZZA_SNAPSHOT_FIXTURE_VALIDATION_PLAN_2026-06-18.md"),
    Path("docs/obsidian/Research/AI_Office_Pizza_Snapshot_Fixture_Validation_Plan.md"),
]
MARKERS = ['Snapshot Fixture Validation Plan', 'documentation only', 'No route creation', 'No database change', 'No migration', 'No runtime gateway integration', 'No live production data access', 'Pizza App remains the source of truth', 'approved readonly snapshots', 'snapshot_id', 'schema_version', 'source_commit', 'generated_at', 'snapshot timestamp', 'checksum', 'staleness policy', 'pagination policy', 'timeout policy', 'data minimization', 'audit trail', 'tenant isolation', 'store isolation', 'safe failure', 'Approval gates', 'Rollback and disable strategy', 'cross-repo readiness summary']
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f"missing document: {doc}")
    text = doc.read_text(encoding="utf-8")
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f"missing marker {marker!r} in {doc}")
    print(f"VALID_DOC {doc}")
print("SMOKE_AI_OFFICE_PIZZA_SNAPSHOT_FIXTURE_VALIDATION_PLAN_DOCS_OK")
