from __future__ import annotations

from typing import Any

from ai_office.contracts import AgentContract, TaskContract
from ai_office.store import InMemoryOfficeStore


def create_default_store() -> InMemoryOfficeStore:
    store = InMemoryOfficeStore()

    supervisor = AgentContract(
        id="agent_supervisor",
        name="Supervisor",
        role="supervisor",
        description="Coordinates office tasks and approvals.",
        capabilities=("plan", "delegate", "audit"),
    )

    auditor = AgentContract(
        id="agent_auditor",
        name="Auditor",
        role="auditor",
        description="Reviews risks, diffs, smokes and release readiness.",
        capabilities=("review", "risk_classify", "approve"),
    )

    local_executor = AgentContract(
        id="agent_local_executor",
        name="Local Executor",
        role="local_executor",
        description="Represents the AI Bridge Local execution lane.",
        capabilities=("local_status_readonly",),
    )

    store.add_agent(supervisor)
    store.add_agent(auditor)
    store.add_agent(local_executor)

    store.add_task(
        TaskContract(
            id="task_mvp_readonly",
            title="Build readonly MVP foundation",
            description="Create agents, tasks and audit events without command execution.",
            status="planned",
            priority=3,
            owner_agent_id=supervisor.id,
            source="bootstrap",
            project_key="ws-ai-office",
        )
    )

    return store


def get_readonly_status(store: InMemoryOfficeStore) -> dict[str, Any]:
    snapshot = store.snapshot()
    return {
        "ok": True,
        "mode": "readonly",
        "agents_count": len(snapshot["agents"]),
        "tasks_count": len(snapshot["tasks"]),
        "audit_events_count": len(snapshot["audit_events"]),
        "execution_enabled": False,
        "database_enabled": False,
        "local_runner_enabled": False,
    }
