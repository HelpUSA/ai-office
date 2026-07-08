from pathlib import Path
DOCS = [
    Path('docs/research/AI_OFFICE_PIZZA_SYNTHETIC_FIXTURE_PLAN_2026-07-08.md'),
    Path('docs/obsidian/Research/AI_Office_Pizza_Synthetic_Fixture_Plan.md'),
]
MARKERS = ['documentation only', 'No route creation', 'No database change', 'No migration', 'No runtime gateway integration', 'No live production data access', 'Pizza App remains the source of truth', 'approved readonly snapshots', 'schema_version', 'snapshot_id', 'source_commit', 'generated_at', 'snapshot timestamp', 'checksum', 'staleness policy', 'pagination policy', 'timeout policy', 'tenant isolation', 'store isolation', 'audit trail', 'rollback and disable strategy', 'safe failure', 'manual approval gate', 'Micro53', 'synthetic fixture', 'synthetic only', 'no real customer messages', 'no payment token', 'no private credential', 'no production queue payload', 'readonly_snapshot_v1_synthetic.json']
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f'missing document: {doc}')
    text = doc.read_text(encoding='utf-8')
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f'missing marker {marker!r} in {doc}')
    print(f'VALID_DOC {doc}')
print('SMOKE_AI_OFFICE_PIZZA_SYNTHETIC_FIXTURE_DOCS_OK')

import json
from pathlib import Path
fixture = Path("tests/fixtures/pizza/readonly_snapshot_v1_synthetic.json")
if not fixture.exists():
    raise AssertionError(f"missing fixture: {fixture}")
data = json.loads(fixture.read_text(encoding="utf-8"))
required = ["snapshot_id","schema_version","source_repository","source_branch","source_commit","generated_at","snapshot_timestamp","tenant_id","store_id","record_count","checksum","staleness_policy","pagination","timeout_policy","data_minimization","audit_trail","records"]
for field in required:
    if field not in data:
        raise AssertionError(f"missing fixture field: {field}")
if data["schema_version"] != "pizza_readonly_snapshot.v1":
    raise AssertionError("unexpected schema_version")
if data["record_count"] != len(data["records"]):
    raise AssertionError("record_count mismatch")
for flag in ["contains_customer_secrets","contains_payment_tokens","contains_private_credentials","contains_production_queue_payloads"]:
    if data["data_minimization"].get(flag) is not False:
        raise AssertionError(f"forbidden data minimization flag not false: {flag}")
if data["data_minimization"].get("synthetic_only") is not True:
    raise AssertionError("fixture must be synthetic only")
print(f"VALID_FIXTURE {fixture}")
