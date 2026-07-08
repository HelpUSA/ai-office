from pathlib import Path
DOCS = [
    Path('docs/research/AI_OFFICE_PIZZA_CROSS_REPO_READINESS_SUMMARY_2026-07-08.md'),
    Path('docs/obsidian/Research/AI_Office_Pizza_Cross_Repo_Readiness_Summary.md'),
]
MARKERS = ['documentation only', 'No route creation', 'No database change', 'No migration', 'No runtime gateway integration', 'No live production data access', 'Pizza App remains the source of truth', 'approved readonly snapshots', 'schema_version', 'snapshot_id', 'source_commit', 'generated_at', 'snapshot timestamp', 'checksum', 'staleness policy', 'pagination policy', 'timeout policy', 'tenant isolation', 'store isolation', 'audit trail', 'rollback and disable strategy', 'safe failure', 'manual approval gate', 'Micro50', 'Micro45', 'Micro46', 'Micro47', 'Micro48', 'Micro49', 'c00f2c1', '2d8c09a', 'bf7c3fc', 'b972da3', '6ffd9f5', 'runtime remains blocked', 'smoke coverage', 'cross-repo readiness summary']
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f'missing document: {doc}')
    text = doc.read_text(encoding='utf-8')
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f'missing marker {marker!r} in {doc}')
    print(f'VALID_DOC {doc}')
print('SMOKE_AI_OFFICE_PIZZA_CROSS_REPO_READINESS_SUMMARY_DOCS_OK')
