from __future__ import annotations

import json
import threading
import time
import urllib.request

from ai_office.http_api import create_server


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=3) as response:
        assert response.status == 200
        data = response.read().decode("utf-8")
        return json.loads(data)


def test_http_api_readonly() -> None:
    server = create_server("127.0.0.1", 0)
    host, port = server.server_address
    base_url = f"http://{host}:{port}"

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        time.sleep(0.1)

        health = get_json(base_url + "/health")
        assert health["ok"] is True
        assert health["service"] == "ws-ai-office"
        assert health["mode"] == "readonly"

        ready = get_json(base_url + "/ready")
        assert ready["ok"] is True
        assert ready["ready"] is True
        assert ready["database_enabled"] is False
        assert ready["execution_enabled"] is False
        assert ready["local_runner_enabled"] is False

        status = get_json(base_url + "/status")
        assert status["ok"] is True
        assert status["agents_count"] == 3
        assert status["tasks_count"] == 1

        agents = get_json(base_url + "/agents")
        assert len(agents["agents"]) == 3

        tasks = get_json(base_url + "/tasks")
        assert len(tasks["tasks"]) == 1

        audit_events = get_json(base_url + "/audit-events")
        assert len(audit_events["audit_events"]) >= 4

    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=3)


if __name__ == "__main__":
    test_http_api_readonly()
    print("SMOKE_HTTP_API_OK")
