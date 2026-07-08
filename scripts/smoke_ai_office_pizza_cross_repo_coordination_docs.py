from pathlib import Path
import subprocess
import sys

PIZZA = Path("D:/dev/pizza")

DOCS = [
    Path("docs/research/AI_OFFICE_PIZZA_CROSS_REPO_SMOKE_COORDINATION_2026-07-08.md"),
    Path("docs/obsidian/Research/AI_Office_Pizza_Cross_Repo_Smoke_Coordination.md"),
]
DOC_MARKERS = [
    "Cross-Repo Smoke Coordination",
    "documentation only",
    "No route creation",
    "No database change",
    "No migration",
    "No runtime gateway integration",
    "No live production data access",
    "Pizza App remains the source of truth",
    "approved readonly snapshots",
    "Strict Pizza approval gate marker validation",
    "approval_state",
    "not_approved",
    "runtime_implementation_allowed",
    "False",
    "live_production_data_access_allowed",
    "gateway_runtime_integration_allowed",
    "database_change_allowed",
    "migration_allowed",
    "approved readonly snapshots",
    "schema_version",
    "snapshot_id",
    "source_commit",
    "generated_at",
    "snapshot timestamp",
    "checksum",
    "staleness policy",
    "pagination policy",
    "timeout policy",
    "tenant isolation",
    "store isolation",
    "audit trail",
    "rollback and disable strategy",
    "disable switch",
    "least privilege",
    "deny by default",
    "safe failure",
]
for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f"missing document: {doc}")
    text = doc.read_text(encoding="utf-8")
    for marker in DOC_MARKERS:
        if marker not in text:
            raise AssertionError(f"missing marker {marker!r} in {doc}")
    print(f"VALID_DOC {doc}")

AI_OFFICE_ARTIFACTS = [
    Path("docs/research/AI_OFFICE_PIZZA_CROSS_REPO_READINESS_SUMMARY_2026-07-08.md"),
    Path("docs/research/AI_OFFICE_PIZZA_APPROVAL_GATE_MANIFEST_2026-07-08.md"),
    Path("docs/research/AI_OFFICE_PIZZA_FIXTURE_SCHEMA_CONTRACT_2026-07-08.md"),
    Path("docs/research/AI_OFFICE_PIZZA_SYNTHETIC_FIXTURE_PLAN_2026-07-08.md"),
    Path("docs/research/AI_OFFICE_PIZZA_CROSS_REPO_SMOKE_COORDINATION_2026-07-08.md"),
    Path("tests/fixtures/pizza/readonly_snapshot_v1_synthetic.json"),
]
for path in AI_OFFICE_ARTIFACTS:
    if not path.exists():
        raise AssertionError(f"missing AI Office artifact: {path}")
    print(f"VALID_AI_OFFICE_ARTIFACT {path}")

PIZZA_EXPECTATIONS = {
    PIZZA / "docs/research/AI_OFFICE_PIZZA_READONLY_SNAPSHOT_DESIGN_2026-06-18.md": [
        "documentation only",
        "No route creation",
        "No database change",
        "No migration",
        "No runtime gateway integration",
        "No live production data access",
        "Pizza App remains the source of truth",
    ],
    PIZZA / "docs/research/AI_OFFICE_PIZZA_READONLY_ROUTE_STAGING_PLAN_2026-06-18.md": [
        "documentation only",
        "No route creation",
        "No database change",
        "No migration",
        "No runtime gateway integration",
        "No live production data access",
        "Pizza App remains the source of truth",
    ],
    PIZZA / "docs/research/AI_OFFICE_PIZZA_READONLY_APPROVAL_GATE_2026-07-07.md": [
        "Readonly Approval Gate",
        "documentation only",
        "No route creation",
        "No database change",
        "No migration",
        "No runtime gateway integration",
        "No live production data access",
        "approval_state",
        "not_approved",
        "runtime_implementation_allowed",
        "False",
        "readonly_snapshot_consumption_allowed",
        "production_route_allowed",
        "live_production_data_access_allowed",
        "gateway_runtime_integration_allowed",
        "database_change_allowed",
        "migration_allowed",
        "approved readonly snapshots",
        "schema_version",
        "snapshot_id",
        "source_commit",
        "generated_at",
        "snapshot timestamp",
        "checksum",
        "staleness policy",
        "pagination policy",
        "timeout policy",
        "tenant isolation",
        "store isolation",
        "audit trail",
        "rollback and disable strategy",
        "disable switch",
        "least privilege",
        "deny by default",
        "safe failure",
        "Pizza App remains the source of truth",
        "AI Office",
        "Micro55",
    ],
}
for path, markers in PIZZA_EXPECTATIONS.items():
    if not path.exists():
        raise AssertionError(f"missing Pizza App artifact: {path}")
    text = path.read_text(encoding="utf-8")
    for marker in markers:
        if marker not in text:
            raise AssertionError(f"missing Pizza marker {marker!r} in {path}")
    print(f"VALID_PIZZA_ARTIFACT {path}")

runtime_guard = PIZZA / "scripts/smoke_ai_office_pizza_readonly_runtime_guard.py"
if runtime_guard.exists():
    subprocess.run([sys.executable, str(runtime_guard)], cwd=str(PIZZA), check=True)

print("SMOKE_AI_OFFICE_PIZZA_CROSS_REPO_COORDINATION_DOCS_OK")
