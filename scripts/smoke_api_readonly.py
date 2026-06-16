from ai_office.api import create_default_store, get_readonly_status


def test_default_store_status() -> None:
    store = create_default_store()
    status = get_readonly_status(store)

    assert status["ok"] is True
    assert status["mode"] == "readonly"
    assert status["agents_count"] == 3
    assert status["tasks_count"] == 1
    assert status["audit_events_count"] >= 4
    assert status["execution_enabled"] is False
    assert status["database_enabled"] is False
    assert status["local_runner_enabled"] is False


def test_snapshot_shape() -> None:
    store = create_default_store()
    snapshot = store.snapshot()

    roles = sorted(agent["role"] for agent in snapshot["agents"])
    assert roles == ["auditor", "local_executor", "supervisor"]

    task = snapshot["tasks"][0]
    assert task["id"] == "task_mvp_readonly"
    assert task["status"] == "planned"
    assert task["project_key"] == "ws-ai-office"


if __name__ == "__main__":
    test_default_store_status()
    test_snapshot_shape()
    print("SMOKE_API_READONLY_OK")
