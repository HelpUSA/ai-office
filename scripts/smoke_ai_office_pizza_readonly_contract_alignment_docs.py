from pathlib import Path

DOCS = [
    Path("docs/research/AI_OFFICE_PIZZA_READONLY_CONTRACT_ALIGNMENT_2026-06-18.md"),
    Path("docs/obsidian/Research/AI_Office_Pizza_Readonly_Contract_Alignment.md"),
]

MARKERS = [
    "Readonly Contract Alignment",
    "documentation only",
    "No route creation",
    "No database change",
    "No migration",
    "No runtime gateway integration",
    "Pizza App remains the source of truth",
    "approved readonly snapshots",
    "Micro41 readonly API contract draft",
    "Micro42 readonly implementation checklist",
    "snapshot consumption plan",
    "Forbidden in this phase",
    "Micro45 in AI Office",
]

for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f"missing document: {doc}")
    text = doc.read_text(encoding="utf-8")
    for marker in MARKERS:
        if marker not in text:
            raise AssertionError(f"missing marker {marker!r} in {doc}")
    print(f"VALID_DOC {doc}")

print("SMOKE_AI_OFFICE_PIZZA_READONLY_CONTRACT_ALIGNMENT_DOCS_OK")
