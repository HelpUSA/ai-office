from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


CommandStatus = Literal[
    "draft",
    "queued",
    "claimed",
    "delivered",
    "acked",
    "failed",
    "cancelled",
]

TaskStatus = Literal[
    "draft",
    "planned",
    "waiting_approval",
    "queued",
    "running",
    "blocked",
    "completed",
    "failed",
    "cancelled",
]

ApprovalStatus = Literal[
    "pending",
    "approved",
    "rejected",
    "expired",
]


@dataclass(frozen=True)
class AgentContract:
    id: str
    name: str
    role: str
    description: str = ""
    status: str = "active"
    capabilities: tuple[str, ...] = field(default_factory=tuple)
    default_model: str | None = None


@dataclass(frozen=True)
class TaskContract:
    id: str
    title: str
    description: str = ""
    status: TaskStatus = "draft"
    priority: int = 5
    owner_agent_id: str | None = None
    source: str = "manual"
    project_key: str | None = None


@dataclass(frozen=True)
class CommandContract:
    id: str
    command_id: str
    action: str
    delivery_kind: str
    payload_json: dict[str, Any] = field(default_factory=dict)
    payload_text: str = ""
    status: CommandStatus = "draft"
    priority: int = 5
    task_id: str | None = None
    source_agent_id: str | None = None
    target_runner_id: str | None = None
    source_chat_id: str | None = None
    target_chat_id: str | None = None

    def is_local_capability(self) -> bool:
        return self.delivery_kind == "local_capability"

    def requires_approval(self) -> bool:
        risky_actions = {
            "deploy",
            "push",
            "git-reset",
            "git-clean",
            "delete-files",
            "db-migration-real",
            "cleanup-real",
        }
        if self.action in risky_actions:
            return True

        command = self.payload_json.get("command")
        if isinstance(command, list):
            joined = " ".join(str(part).lower() for part in command)
        else:
            joined = str(command or "").lower()

        risky_fragments = [
            "git reset",
            "git clean",
            "remove-item",
            "rm -rf",
            "drop table",
            "delete from",
            "railway up",
            "vercel deploy",
        ]
        return any(fragment in joined for fragment in risky_fragments)


@dataclass(frozen=True)
class LocalRunResultContract:
    command_id: str
    success: bool
    return_code: int
    stdout: str = ""
    stderr: str = ""
    result_is_final: bool = True
    chat_can_continue: bool = True
    next_action: str = "continue_next_activity"


def build_local_run_command(
    *,
    command_id: str,
    source_chat_id: str,
    cwd: str,
    command: list[str],
    timeout_seconds: int = 120,
) -> CommandContract:
    return CommandContract(
        id=command_id,
        command_id=command_id,
        action="run-command",
        delivery_kind="local_capability",
        source_chat_id=source_chat_id,
        target_chat_id="gateway-brain-supervisor",
        payload_json={
            "cwd": cwd,
            "command": command,
            "timeout_seconds": timeout_seconds,
        },
        status="draft",
    )
