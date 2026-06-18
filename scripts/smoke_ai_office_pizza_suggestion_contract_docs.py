from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "docs/research/AI_OFFICE_PIZZA_APP_SUGGESTION_CONTRACT_DRAFT_2026-06-18.md",
    ROOT / "docs/obsidian/Research/AI_Office_Pizza_App_Suggestion_Contract_Draft.md",
]

REQUIRED_MARKERS = [
    "documentation only",
    "suggestion contract draft",
    "suggestion only",
    "human approval required",
    "Pizza App remains the source of truth",
    "AI Office may generate suggestions",
    "requires_human_approval: true",
    "execution_allowed: false",
    "approval_status: draft",
    "Delayed order attention",
    "Promotion idea",
    "Menu review",
    "Customer follow-up draft",
    "Stock and purchasing attention",
    "Finance review",
    "no mutation of orders",
    "no payment capture",
    "no refund",
    "no coupon creation",
    "no campaign sending",
    "no menu price change",
    "no customer message sending",
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
    print("SMOKE_AI_OFFICE_PIZZA_SUGGESTION_CONTRACT_DOCS_OK")

if __name__ == "__main__":
    main()
