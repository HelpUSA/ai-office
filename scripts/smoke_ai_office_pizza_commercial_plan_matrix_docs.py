from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "docs/research/AI_OFFICE_PIZZA_APP_COMMERCIAL_PLAN_MATRIX_2026-06-18.md",
    ROOT / "docs/obsidian/Research/AI_Office_Pizza_App_Commercial_Plan_Matrix.md",
]

REQUIRED_MARKERS = [
    "documentation only",
    "commercial plan matrix",
    "commercial research only",
    "AI-powered restaurant operating platform",
    "Pizza App remains the source of truth",
    "Basic",
    "Pro",
    "Premium",
    "Enterprise",
    "readonly only",
    "suggestion only",
    "human approval required",
    "requires_human_approval: true",
    "execution_allowed: false",
    "approval_status: draft",
    "virtual manager",
    "multi-store reporting concept",
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
    "no direct database query by AI Office",
    "no run-command execution from app runtime",
    "no send-chat-message execution from app runtime",
    "no db-query",
    "no file-ops",
    "no codex-analyze",
    "no mutation of orders",
    "no payment capture",
    "no refund",
    "no coupon creation",
    "no campaign sending",
    "no menu price change",
    "no customer message sending",
]

def main() -> None:
    for doc in DOCS:
        if not doc.exists():
            raise AssertionError(f"missing doc: {doc}")
        text = doc.read_text(encoding="utf-8")
        for marker in REQUIRED_MARKERS:
            if marker not in text:
                raise AssertionError(f"missing marker {marker!r} in {doc}")
    print("SM_AI_OFFICE_PIZZA_COMMERCIAL_PLAN_MATRIX_DOCS_OK")

if __name__ == "__main__":
    main()
