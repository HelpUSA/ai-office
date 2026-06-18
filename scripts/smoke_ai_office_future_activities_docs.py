from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    ROOT / "docs/AI_OFFICE_PROJECT_INDEX_2026-06-18.md",
    ROOT / "docs/research/AI_OFFICE_FUTURE_ACTIVITIES_AND_PARALLEL_RESOURCES_2026-06-18.md",
    ROOT / "docs/obsidian/Research/AI_Office_Future_Activities_And_Parallel_Resources.md",
]
REQUIRED = [
    "AI Office Future Activities and Parallel Resources",
    "docs-only",
    "smoke-only",
    "readonly",
    "no route creation",
    "no database change",
    "no migration",
    "no runtime gateway integration",
    "Micro42 - Pizza readonly implementation checklist",
    "Micro43 - AI Office contract alignment",
    "Micro44 - Pizza docs smoke consolidation",
    "Micro45 - AI Office snapshot consumption plan",
    "Micro46 - Pizza snapshot design draft",
    "Micro47 - Security and authorization matrix",
    "Micro48 - Staging rollout plan",
    "Parallel resources to add",
    "no git add dot",
    "Decision rule for leaving docs-only",
]

def main():
    for doc in DOCS:
        if not doc.exists():
            raise AssertionError(f"missing doc: {doc}")
        text = doc.read_text(encoding="utf-8")
        for marker in ["docs-only", "smoke-only", "readonly", "no runtime gateway integration"]:
            if marker not in text:
                raise AssertionError(f"missing base marker {marker!r} in {doc}")
    for doc in DOCS[1:]:
        text = doc.read_text(encoding="utf-8")
        for marker in REQUIRED:
            if marker not in text:
                raise AssertionError(f"missing roadmap marker {marker!r} in {doc}")
    print("SMOKE_AI_OFFICE_FUTURE_ACTIVITIES_DOCS_OK")

if __name__ == "__main__":
    main()
