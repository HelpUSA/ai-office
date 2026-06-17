from __future__ import annotations

from pathlib import Path
import re
from datetime import datetime

OFFICE_ROOT = Path(r"D:\dev\autocode\ai-office")
BRIDGE_ROOT = Path(r"D:\dev\autocode\ai-bridge")

REPORT_PATH = OFFICE_ROOT / "docs" / "research" / "WS_AI_OFFICE_PHASE_B_GATEWAY_CONTRACT_EVIDENCE_2026-06-17.md"
OBSIDIAN_PATH = OFFICE_ROOT / "docs" / "obsidian" / "Research" / "Phase_B_Gateway_Contract_Evidence.md"

SOURCE_FILES = [
    "apps/watcher-api/src/server.mjs",
    "apps/watcher-api/src/message-queue.mjs",
    "apps/watcher-api/src/broker.mjs",
    "extension-next/background.js",
    "extension-next/content_script.js",
    "extension-next/capability_router.js",
]

ROUTES = [
    "/bridge/next-action",
    "/bridge/events",
    "/bridge/acks",
    "/claim",
    "/ack",
]

FIELDS = [
    "command_id",
    "conversation_id",
    "source_chat_id",
    "target_chat_id",
    "destino",
    "origem",
    "status",
    "queued",
    "delivered",
    "acked",
    "failed",
    "result_is_final",
    "no_reply",
    "attempts",
    "last_error",
    "action",
    "type",
    "delivery_kind",
    "payload",
    "command",
    "cwd",
    "timeout_seconds",
    "event_type",
    "message_kind",
    "chat_id",
    "text",
    "result",
    "error",
    "created_at",
]

DANGEROUS_TERMS = [
    "exec(",
    "spawn(",
    "execFile(",
    "git-op",
    "db-query",
    "file-ops",
    "codex-analyze",
    "cleanup",
    "delete from",
    "drop table",
    "rm -rf",
    "git reset",
    "git clean",
]

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def line_matches(text: str, terms: list[str]) -> list[tuple[int, str, str]]:
    rows = []
    for idx, line in enumerate(text.splitlines(), start=1):
        lowered = line.lower()
        for term in terms:
            if term.lower() in lowered:
                rows.append((idx, term, line.rstrip()))
                break
    return rows

def route_method_guess(line: str, route: str) -> str:
    compact = line.replace(" ", "")
    if f'.get("{route}"' in compact or f".get('{route}'" in compact:
        return "GET"
    if f'.post("{route}"' in compact or f".post('{route}'" in compact:
        return "POST"
    if f'GET {route}' in line:
        return "GET"
    if f'POST {route}' in line:
        return "POST"
    return "unknown"

def extract_route_rows(files: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    for rel, text in files.items():
        for idx, line in enumerate(text.splitlines(), start=1):
            for route in ROUTES:
                if route in line:
                    rows.append({
                        "route": route,
                        "method": route_method_guess(line, route),
                        "file": rel,
                        "line": str(idx),
                        "evidence": line.strip(),
                    })
    return rows

def extract_field_rows(files: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    seen = set()
    for rel, text in files.items():
        for idx, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            for field in FIELDS:
                if field.lower() in lowered:
                    key = (field, rel, idx)
                    if key not in seen:
                        seen.add(key)
                        rows.append({
                            "field": field,
                            "file": rel,
                            "line": str(idx),
                            "evidence": line.strip(),
                        })
                    break
    return rows

def extract_status_rows(files: dict[str, str]) -> list[dict[str, str]]:
    statuses = ["queued", "delivered", "acked", "failed", "running", "completed", "cancelled", "stale"]
    rows = []
    seen = set()
    for rel, text in files.items():
        for idx, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            for status in statuses:
                if status in lowered:
                    key = (status, rel, idx)
                    if key not in seen:
                        seen.add(key)
                        rows.append({
                            "status": status,
                            "file": rel,
                            "line": str(idx),
                            "evidence": line.strip(),
                        })
                    break
    return rows

def extract_danger_rows(files: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    for rel, text in files.items():
        for idx, term, line in line_matches(text, DANGEROUS_TERMS):
            rows.append({
                "term": term,
                "file": rel,
                "line": str(idx),
                "evidence": line.strip(),
            })
    return rows

def md_table(headers: list[str], rows: list[dict[str, str]], limit: int = 80) -> list[str]:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows[:limit]:
        cells = []
        for header in headers:
            value = str(row.get(header, ""))
            value = value.replace("|", "\\|").replace("\n", " ")
            if len(value) > 180:
                value = value[:177] + "..."
            cells.append(value)
        out.append("| " + " | ".join(cells) + " |")
    if len(rows) > limit:
        out.append(f"| ... | ... | ... | ... |")
        out.append(f"| truncated | showing {limit} of {len(rows)} rows | | |")
    return out

def main() -> None:
    files: dict[str, str] = {}

    missing = []
    for rel in SOURCE_FILES:
        path = BRIDGE_ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        files[rel] = read_text(path)

    route_rows = extract_route_rows(files)
    field_rows = extract_field_rows(files)
    status_rows = extract_status_rows(files)
    danger_rows = extract_danger_rows(files)

    lines: list[str] = []
    lines.append("# WS AI Office Phase B Gateway Contract Evidence")
    lines.append("")
    lines.append("Status: readonly evidence extraction only.")
    lines.append("")
    lines.append("This document was generated from local AI Bridge source files without enabling gateway integration, command execution, ACK, queue claim, database writes, file operations or git operations.")
    lines.append("")
    lines.append("## Source roots")
    lines.append("")
    lines.append(f"- WS AI Office: `{OFFICE_ROOT}`")
    lines.append(f"- AI Bridge reference: `{BRIDGE_ROOT}`")
    lines.append("")
    lines.append("## Safety assertion")
    lines.append("")
    lines.append("- Readonly source inspection only.")
    lines.append("- No AI Bridge process started.")
    lines.append("- No route called.")
    lines.append("- No queue polled.")
    lines.append("- No ACK posted.")
    lines.append("- No command created.")
    lines.append("- No local execution enabled.")
    lines.append("")
    lines.append("## Files inspected")
    lines.append("")
    for rel in SOURCE_FILES:
        status = "present" if rel in files else "missing"
        lines.append(f"- {status}: `{rel}`")
    lines.append("")
    if missing:
        lines.append("## Missing files")
        lines.append("")
        for rel in missing:
            lines.append(f"- `{rel}`")
        lines.append("")
    lines.append("## Route evidence")
    lines.append("")
    if route_rows:
        lines.extend(md_table(["method", "route", "file", "line", "evidence"], route_rows, limit=120))
    else:
        lines.append("No route evidence found for target Phase B routes.")
    lines.append("")
    lines.append("## Field evidence")
    lines.append("")
    if field_rows:
        lines.extend(md_table(["field", "file", "line", "evidence"], field_rows, limit=160))
    else:
        lines.append("No field evidence found.")
    lines.append("")
    lines.append("## Status lifecycle evidence")
    lines.append("")
    if status_rows:
        lines.extend(md_table(["status", "file", "line", "evidence"], status_rows, limit=120))
    else:
        lines.append("No status evidence found.")
    lines.append("")
    lines.append("## Dangerous capability evidence")
    lines.append("")
    lines.append("The following references are evidence for risk classification only, not approval to expose these capabilities in WS AI Office.")
    lines.append("")
    if danger_rows:
        lines.extend(md_table(["term", "file", "line", "evidence"], danger_rows, limit=120))
    else:
        lines.append("No dangerous capability evidence found in inspected files.")
    lines.append("")
    lines.append("## Phase B decision")
    lines.append("")
    lines.append("Evidence extraction is complete for contract-study purposes.")
    lines.append("")
    lines.append("No runtime gateway integration is approved by this document.")
    lines.append("")
    lines.append("## Next recommended micro")
    lines.append("")
    lines.append("Create a WS AI Office internal gateway contract schema draft based on this evidence, still documentation only.")
    lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OBSIDIAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    OBSIDIAN_PATH.write_text("\n".join(lines), encoding="utf-8")

    print("EXTRACT_AI_BRIDGE_GATEWAY_CONTRACT_EVIDENCE_OK")
    print(f"files_present={len(files)}")
    print(f"files_missing={len(missing)}")
    print(f"route_rows={len(route_rows)}")
    print(f"field_rows={len(field_rows)}")
    print(f"status_rows={len(status_rows)}")
    print(f"danger_rows={len(danger_rows)}")
    print(f"report={REPORT_PATH}")
    print(f"obsidian={OBSIDIAN_PATH}")

if __name__ == "__main__":
    main()
