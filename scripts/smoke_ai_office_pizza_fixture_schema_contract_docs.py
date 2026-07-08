from pathlib import Path
DOCS = [
    Path('docs/research/AI_OFFICE_PIZZA_FIXTURE_SCHEMA_CONTRACT_2026-07-08.md'),
    Path('docs/obsidian/Research/AI_Office_Pizza_Fixture_Schema_Contract.md'),
]
MARKERS = ['documentation only', 'No route creation', 'No database change', 'No migration', 'No runtime gateway integration', 'No live production data access', 'Pizza App remains the source of truth', 'approved readonly snapshots', 'schema_version', 'snapshot_id', 'source_commit', 'generated_at', 'snapshot timestamp', 'checksum', 'staleness policy', 'pagination policy', 'timeout policy', 'tenant isolation', 'store isolation', 'audit trail', 'rollback and disable strategy', 'safe failure', 'manual approval gate', 'Micro52', 'source_repository', 'source_branch', 'source_commit', 'tenant_id', 'store_id', 'record_count', 'records', 'data minimization', 'max_age_seconds', 'timeout_ms']
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f'missing document: {doc}')
    text = doc.read_text(encoding='utf-8')
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f'missing marker {marker!r} in {doc}')
    print(f'VALID_DOC {doc}')
print('SMOKE_AI_OFFICE_PIZZA_FIXTURE_SCHEMA_CONTRACT_DOCS_OK')
