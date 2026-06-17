from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlparse

from ai_office.service import create_default_store, get_readonly_status


def json_bytes(payload: dict[str, Any], status: int = 200) -> bytes:
    body = {
        "status_code": status,
        **payload,
    }
    return json.dumps(body, ensure_ascii=False, sort_keys=True).encode("utf-8")


class OfficeHttpHandler(BaseHTTPRequestHandler):
    server_version = "WSAIOfficeHTTP/0.1"

    def _write_json(self, status: int, payload: dict[str, Any]) -> None:
        data = json_bytes(payload, status=status)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: Any) -> None:
        # Keep smoke output deterministic and quiet.
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path

        store = self.server.office_store  # type: ignore[attr-defined]

        if path == "/health":
            self._write_json(
                200,
                {
                    "ok": True,
                    "service": "ws-ai-office",
                    "mode": "readonly",
                },
            )
            return

        if path == "/ready":
            self._write_json(
                200,
                {
                    "ok": True,
                    "ready": True,
                    "database_enabled": False,
                    "execution_enabled": False,
                    "local_runner_enabled": False,
                },
            )
            return

        if path == "/status":
            self._write_json(200, get_readonly_status(store))
            return

        if path == "/agents":
            self._write_json(
                200,
                {
                    "ok": True,
                    "agents": store.snapshot()["agents"],
                },
            )
            return

        if path == "/tasks":
            self._write_json(
                200,
                {
                    "ok": True,
                    "tasks": store.snapshot()["tasks"],
                },
            )
            return

        if path == "/audit-events":
            self._write_json(
                200,
                {
                    "ok": True,
                    "audit_events": store.snapshot()["audit_events"],
                },
            )
            return

        self._write_json(
            404,
            {
                "ok": False,
                "error": "not_found",
                "path": path,
            },
        )


class OfficeHttpServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int]) -> None:
        super().__init__(server_address, OfficeHttpHandler)
        self.office_store = create_default_store()


def create_server(host: str = "127.0.0.1", port: int = 8787) -> OfficeHttpServer:
    return OfficeHttpServer((host, port))


def main() -> None:
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8787"))
    server = create_server(host=host, port=port)
    actual_host, actual_port = server.server_address
    print(f"WS_AI_OFFICE_HTTP_API_LISTENING http://{actual_host}:{actual_port}")
    server.serve_forever()


if __name__ == "__main__":
    main()

