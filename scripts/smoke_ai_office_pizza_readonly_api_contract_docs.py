from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "docs/research/AI_OFFICE_PIZZA_APP_READONLY_API_CONTRACT_DRAFT_2026-06-17.md",
    ROOT / "docs/obsidian/Research/AI_Office_Pizza_App_Readonly_API_Contract_Draft.md",
]

REQUIRED_MARKERS = [
    "documentation only",
    "readonly API contract draft",
    "Pizza App remains the source of truth",
    "AI Office may read approved operational snapshots",
    "AI Office must not mutate Pizza App state",
    "GET /ai-office/readonly/orders/summary",
    "GET /ai-office/readonly/orders/recent",
    "GET /ai-office/readonly/orders/delayed",
    "GET /ai-office/readonly/menu/summary",
    "GET /ai-office/readonly/customers/summary",
    "GET /ai-office/readonly/finance/daily-summary",
    "readonly: true",
    "no mutation of orders",
    "no payment capture",
    "no refund",
    "no coupon creation",
    "no campaign sending",
    "no production queue read",
    "no direct database query by AI Office",
    "no command execution from app runtime",
    "no live gateway polling",
    "no runtime gateway integration",
    "database_enabled=false",
    "execution_enabled=false",
    "local_runner_enabled=false",
    "gateway_integration_enabled=false",
    "no live polling",
    "no real claim",
    "no real ack",
    "ACK posting remains disabled",
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
    print("SM_AI_OFFICE_PIZZA_READONLY_API_CONTRACT_DOCS_OK")

if __name__ == "__main__":
    main()
