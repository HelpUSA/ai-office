from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "docs/research/AI_OFFICE_PIZZA_APP_COMMERCIAL_INTEGRATION_RESEARCH_2026-06-17.md",
    ROOT / "docs/obsidian/Research/AI_Office_Pizza_App_Commercial_Integration.md",
]

REQUIRED_MARKERS = [
    "documentation only",
    "commercial research only",
    "Pizza App is the system that executes the restaurant operation",
    "AI Office is the intelligent office layer",
    "AI-powered restaurant operating platform",
    "virtual AI manager",
    "Phase 1 - readonly",
    "Phase 2 - suggestions",
    "Phase 3 - controlled execution",
    "Phase 4 - virtual manager",
    "no runtime gateway integration",
    "database_enabled=false",
    "execution_enabled=false",
    "local_runner_enabled=false",
    "gateway_integration_enabled=false",
    "no live polling",
    "no real claim",
    "no real ack",
    "ACK posting remains disabled",
    "no production queue read",
    "no run-command execution from app runtime",
    "no send-chat-message execution from app runtime",
    "no db-query",
    "no file-ops",
    "no codex-analyze",
]

def main() -> None:
    for doc in DOCS:
        if not doc.exists():
            raise AssertionError(f"missing doc: {doc}")
        text = doc.read_text(encoding="utf-8")
        for marker in REQUIRED_MARKERS:
            if marker not in text:
                raise AssertionError(f"missing marker {marker!r} in {doc}")
    print("SMOKE_AI_OFFICE_PIZZA_COMMERCIAL_INTEGRATION_DOCS_OK")

if __name__ == "__main__":
    main()
