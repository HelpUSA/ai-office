from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT  / "docs" / "research" / "WS_AI_OFFICE_PHASE_B_GATEWAY_CONTRACT_EVIDENCE_2026-06-17.md",
    ROOT / "docs" / "research" / "WS_AI_OFFICE_INTERNAL_GATEWAY_CONTRACT_SCHEMA_DRAFT_2026-06-17.md",
    ROOT / "docs" / "obsidian" / "Research" / "Phase_B_Gateway_Contract_Evidence.md",
    ROOT / "docs" / "obsidian" / "Research" / "Internal_Gateway_Contract_Schema_Draft.md",
]

REQUIRED_TEXT = [
    "readonly evidence extraction only",
    "documentation only",
    "No runtime gateway integration",
    "database_enabled=false",
    "execution_enabled=false",
    "gateway_integration_enabled=false",
    "ACK posting remains disabled",
    "does not approve runtime gateway integration",
]

def main():
    missing = [str(path) for path in DOCS if not path.exists()]
    assert not missing, "missing docs: " + ", ".join(missing)
    combined = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in DOCS)
    for text in REQUIRED_TEXT:
        assert text in combined, "missing required text: " + text
    for text in ["git-op", "db-query", "file-ops", "codex-analyze", "cleanup"]:
        assert text in combined, "missing blocked capability: " + text
    print("SMOKE_GATEWAY_CONTRACT_SCHEMA_DOCS_OK")

if __name__ == "__main__":
    main()
