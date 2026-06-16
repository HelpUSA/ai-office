from __future__ import annotations

from dataclasses import asdict
from typing import Any

from ai_office.contracts import AgentContract, TaskContract


class InMemoryOfficeStore:
    """Small readonly-first store for MVP smoke tests.

    This store is intentionally in-memory.
    It does not connect to a database and does not execute commands.
    """

    def __init__(self) -> None:
        self._agents: dict[str, AgentContract] = {}
        self._tasks: dict[str, TaskContract] = {}
        self._audit_events: list[dict[str, Any]] = []

    def add_agent(self, agent: AgentContract) -> AgentContract:
        if agent.id in self._agents:
            raise ValueError(f"agent already exists: {agent.id}")
        self._agents[agent.id] = agent
        self.add_audit_event(
            event_type="agent.created",
            actor="system",
            payload_json={"agent_id": agent.id, "role": agent.role},
        )
        return agent

    def list_agents(self) -> list[AgentContract]:
        return list(self._agents.values())

    def get_agent(self, agent_id: str) -> AgentContract | None:
        return self._agents.get(agent_id)

    def add_task(self, task: TaskContract) -> TaskContract:
        if task.id in self._tasks:
            raise ValueError(f"task already exists: {task.id}")
        if task.owner_agent_id and task.owner_agent_id not in self._agents:
            raise ValueError(f"owner agent not found: {task.owner_agent_id}")
        self._tasks[task.id] = task
        self.add_audit_event(
            event_type="task.created",
            actor="system",
            task_id=task.id,
            payload_json={"task_id": task.id, "status": task.status},
        )
        return task

    def list_tasks(self) -> list[TaskContract]:
        return list(self._tasks.values())

    def get_task(self, task_id: str) -> TaskContract | None:
        return self._tasks.get(task_id)

    def add_audit_event(
        self,
        *,
        event_type: str,
        actor: str,
        task_id: str | None = None,
        command_id: str | None = None,
        payload_json: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        event = {
            "id": f"audit_{len(self._audit_events) + 1:06d}",
            "event_type": event_type,
            "actor": actor,
            "task_id": task_id,
            "command_id": command_id,
            "payload_json": payload_json or {},
        }
        self._audit_events.append(event)
        return event

    def list_audit_events(self) -> list[dict[str, Any]]:
        return list(self._audit_events)

    def snapshot(self) -> dict[str, Any]:
        return {
            "agents": [asdict(agent) for agent in self.list_agents()],
            "tasks": [asdict(task) for task in self.list_tasks()],
            "audit_events": self.list_audit_events(),
        }
