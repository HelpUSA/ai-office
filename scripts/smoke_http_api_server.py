from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
import urllib.request


def find_free_port() -> int:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    _, port = sock.getsockname()
    sock.close()
    return int(port)


def get_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=5) as response:
        assert response.status == 200
        return json.loads(response.read().decode("utf-8"))


def wait_for_health(base_url: str, timeout_seconds: float = 8.0) -> dict:
    deadline = time.time() + timeout_seconds
    last_error = None

    while time.time() < deadline:
        try:
            return get_json(base_url + "/health")
        except Exception as exc:
            last_error = exc
            time.sleep(0.2)

    raise RuntimeError(f"server did not become healthy: {last_error}")


def main() -> None:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    port = find_free_port()
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.join(root, "src")
    env["HOST"] = "127.0.0.1"
    env["PORT"] = str(port)

    process = subprocess.Popen(
        [sys.executable, "-m", "ai_office.http_api"],
        cwd=root,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    base_url = f"http://127.0.0.1:{port}"

    try:
        health = wait_for_health(base_url)
        assert health["ok"] is True
        assert health["service"] == "ws-ai-office"

        ready = get_json(base_url + "/ready")
        assert ready["ready"] is True
        assert ready["database_enabled"] is False
        assert ready["execution_enabled"] is False

        status = get_json(base_url + "/status")
        assert status["mode"] == "readonly"
        assert status["agents_count"] == 3

        print("SMOKE_HTTP_API_SERVER_OK")
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)

        stdout, stderr = process.communicate()
        if process.returncode not in (0, -15, 1):
            print("SERVER_STDOUT")
            print(stdout)
            print("SERVER_STDERR")
            print(stderr)


if __name__ == "__main__":
    main()
