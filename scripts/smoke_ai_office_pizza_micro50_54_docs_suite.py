import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "scripts/smoke_ai_office_pizza_cross_repo_readiness_summary_docs.py",
    "scripts/smoke_ai_office_pizza_approval_gate_manifest_docs.py",
    "scripts/smoke_ai_office_pizza_fixture_schema_contract_docs.py",
    "scripts/smoke_ai_office_pizza_synthetic_fixture_docs.py",
    "scripts/smoke_ai_office_pizza_cross_repo_coordination_docs.py",
    "scripts/smoke_ai_office_pizza_security_authorization_matrix_docs.py",
    "scripts/smoke_ai_office_pizza_snapshot_consumption_plan_docs.py",
    "scripts/smoke_ai_office_pizza_snapshot_fixture_validation_plan_docs.py",
    "scripts/smoke_ai_office_pizza_readonly_contract_alignment_docs.py",
]
for script in SCRIPTS:
    path = Path(script)
    if not path.exists():
        raise AssertionError(f"missing suite script: {path}")
    subprocess.run([sys.executable, str(path)], check=True)
print("SMOKE_AI_OFFICE_PIZZA_MICRO50_54_DOCS_SUITE_OK")
