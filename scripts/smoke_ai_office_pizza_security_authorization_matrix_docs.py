from pathlib import Path
DOCS=[Path('docs/research/AI_OFFICE_PIZZA_SECURITY_AUTHORIZATION_MATRIX_2026-06-18.md'),Path('docs/obsidian/Research/AI_Office_Pizza_Security_Authorization_Matrix.md')]
MARKERS=['Security and Authorization Matrix', 'documentation only', 'No route creation', 'No database change', 'No migration', 'No runtime gateway integration', 'No live production data access', 'Pizza App remains the source of truth', 'approved readonly snapshots', 'tenant isolation', 'store isolation', 'Least privilege', 'Deny by default', 'schema_version', 'source_commit', 'snapshot timestamp', 'checksum', 'staleness', 'pagination', 'timeout', 'audit trail', 'rollback and disable strategy', 'Micro48 in Pizza App', 'Micro49 in AI Office']
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f'missing document: {doc}')
    text=doc.read_text(encoding='utf-8')
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f'missing marker {marker!r} in {doc}')
    print(f'VALID_DOC {doc}')
print('SMOKE_AI_OFFICE_PIZZA_SECURITY_AUTHORIZATION_MATRIX_DOCS_OK')
