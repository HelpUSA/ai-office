from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "docs" / "research" / "WS_AI_OFFICE_WATCHER_USAGE_LESSONS_2026-06-17.md",
    ROOT / "docs" / "obsidian" / "Research" / "Watcher_Usage_Lessons.md",
]

REQUIRED_TEXT = [
    "target_chat_id=gateway-brain-supervisor",
    "delivery_kind=local_capability",
    "delivery_kind=inter_agent_message",
    "message as a top-level field",
    "documentation only",
    "database_enabled=false",
    "execution_enabled=false",
    "local_runner_enabled=false",
    "gateway_integration_enabled=false",
    "no runtime gateway integration",
    "no real DB execution",
    "no local runner execution",
    "no real claim",
    "no real ack",
    "ACK posting remains disabled",
]


def main():
    missing = [str(path) for path in DOCS if not path.exists()]
    assert not missing, "missing docs: " + ", ".join(missing)

    for path in DOCS:
        text = path.read_text(encoding="utf-8", errors="replace")
        for required in REQUIRED_TEXT:
            assert required in text, f"missing required text in {path}: {required}"

    print("SMOKE_WATCHER_USAGE_LESSONS_DOCS_OK")


if __name__ == "__main__":
    main()
