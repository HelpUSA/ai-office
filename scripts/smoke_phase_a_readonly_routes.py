from http.server import HTTPServer
from threading import Thread
from urllib.request import urlopen
import json

from ai_office.http_api import (
    OfficeHttpHandler,
    create_default_store,
    phase_a_bridge_health_payload,
    phase_a_compatibility_routes_payload,
    phase_a_gateway_status_payload,
    phase_a_safety_payload,
    phase_a_storage_status_payload,
)


def assert_false(payload, key):
    assert payload.get(key) is False, f"{key} must remain false: {payload}"


def get_json(base_url, path):
    with urlopen(base_url + path, timeout=5) as response:
        assert response.status == 200
        return json.loads(response.read().decode("utf-8"))


def main():
    storage = phase_a_storage_status_payload()
    assert storage["ok"] is True
    assert storage["storage_mode"] == "in_memory"
    assert_false(storage, "database_enabled")
    assert_false(storage, "database_configured")

    bridge = phase_a_bridge_health_payload()
    assert bridge["ok"] is True
    assert bridge["service"] == "ws-ai-office"
    assert bridge["bridge_compatibility"] == "planned"
    assert_false(bridge, "gateway_integration_enabled")
    assert_false(bridge, "execution_enabled")

    gateway = phase_a_gateway_status_payload()
    assert gateway["ok"] is True
    assert gateway["gateway_source"] == "ai-bridge"
    assert gateway["gateway_mode"] == "not_configured"
    assert_false(gateway, "gateway_integration_enabled")
    assert_false(gateway, "can_poll")
    assert_false(gateway, "can_ack")
    assert_false(gateway, "can_execute")

    routes = phase_a_compatibility_routes_payload()
    assert routes["ok"] is True
    assert routes["phase"] == "A_readonly"
    for route in ["/storage-status", "/bridge/health", "/gateway/status", "/compatibility/routes", "/safety"]:
        assert route in routes["implemented"], route
    for blocked in ["/bridge/commands", "/bridge/next-action", "/bridge/events", "/bridge/acks", "/git-op", "/db-query", "/file-ops", "/codex-analyze", "/cleanup"]:
        assert blocked in routes["blocked"], blocked

    safety = phase_a_safety_payload()
    assert safety["ok"] is True
    assert_false(safety, "database_enabled")
    assert_false(safety, "execution_enabled")
    assert_false(safety, "local_runner_enabled")
    assert_false(safety, "gateway_integration_enabled")
    for category in ["controlled_mutation", "gateway_extension", "execution_dangerous", "debug_admin"]:
        assert category in safety["blocked_categories"], category

    server = HTTPServer(("127.0.0.1", 0), OfficeHttpHandler)
    server.office_store = create_default_store()
    port = server.server_address[1]
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        base_url = f"http://127.0.0.1:{port}"
        assert get_json(base_url, "/storage-status")["storage_mode"] == "in_memory"
        assert get_json(base_url, "/bridge/health")["bridge_compatibility"] == "planned"
        assert get_json(base_url, "/gateway/status")["can_execute"] is False
        assert get_json(base_url, "/compatibility/routes")["phase"] == "A_readonly"
        assert get_json(base_url, "/safety")["execution_enabled"] is False
        assert get_json(base_url, "/safety?check=1")["execution_enabled"] is False
    finally:
        server.shutdown()
        server.server_close()

    print("SMOKE_PHASE_A_READONLY_ROUTES_OK")


if __name__ == "__main__":
    main()
