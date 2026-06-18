from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    ROOT  / "docs/research/AI_OFFICE_PIZZA_APP_PHASE1_INTEGRATION_READINESS_CHECKLIST_2026-06-18.md",
    ROOT / "docs/obsidian/Research/AI_Office_Pizza_App_Phase1_Integration_Readiness_Checklist.md",
]
REQUIRED = ['documentation only', 'Phase 1 Integration Readiness Checklist', 'Phase 1 is readonly only', 'Pizza App remains the source of truth', 'AI Office may only read approved operational snapshots', 'AI Office must not mutate Pizza App state', 'GET /ai-office/readonly/orders/summary', 'GET /ai-office/readonly/finance/daily-summary', 'Authentication and authorization', 'Data minimization', 'Snapshot behavior', 'Auditability', 'Rate limits and safety limits', 'Test environment first', 'database_enabled=false', 'execution_enabled=false', 'local_runner_enabled=false', 'gateway_integration_enabled=false', 'no runtime gateway integration', 'no live polling', 'no real claim', 'no real ack', 'ACK posting remains disabled', 'no production queue read', 'no direct database query by AI Office', 'no command execution from app runtime', 'no run-command execution from app runtime', 'no send-chat-message execution from app runtime', 'no db-query', 'no file-ops', 'no codex-analyze', 'no mutation of orders', 'no payment capture', 'no refund', 'no coupon creation', 'no campaign sending', 'no customer message sending', 'Pizza App repository readonly discovery']

def main():
    for doc in DOCS:
        if not doc.exists():
            raise AssertionError(f"missing doc: {doc}")
        text = doc.read_text(encoding="utf-8")
        for marker in REQUIRED:
            if marker not in text:
                raise AssertionError(f"missing marker {marker!r} in {doc}")
    print("SMOKE_AI_OFFICE_PIZZA_PHASE1_INTEGRATION_READINESS_DOCS_OK")

if __name__ == "__main__":
    main()
