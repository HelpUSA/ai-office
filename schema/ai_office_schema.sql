-- WS AI Office - Initial Schema
-- Status: design-first schema, not yet applied to production.
-- Base concepts:
-- - AI Bridge web/API: cloud queue, command_id, source_chat_id, target_chat_id, delivery_kind, payload_json, claim/ack.
-- - AI Bridge Local: local runner, run-command, local_capability, AI_LOCAL_RUN result shape.

create schema if not exists office;

create table if not exists office.agents (
    id text primary key,
    name text not null,
    role text not null,
    description text not null default '',
    status text not null default 'active',
    capabilities jsonb not null default '[]'::jsonb,
    default_model text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists office.tasks (
    id text primary key,
    title text not null,
    description text not null default '',
    status text not null default 'draft',
    priority integer not null default 5,
    owner_agent_id text references office.agents(id),
    source text not null default 'manual',
    project_key text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    completed_at timestamptz
);

create table if not exists office.commands (
    id text primary key,
    command_id text not null unique,
    task_id text references office.tasks(id),
    source_agent_id text references office.agents(id),
    target_runner_id text,
    source_chat_id text,
    target_chat_id text,
    action text not null,
    delivery_kind text not null,
    payload_json jsonb not null default '{}'::jsonb,
    payload_text text not null default '',
    status text not null default 'draft',
    priority integer not null default 5,
    created_at timestamptz not null default now(),
    claimed_at timestamptz,
    delivered_at timestamptz,
    acked_at timestamptz,
    failed_at timestamptz
);

create table if not exists office.executions (
    id text primary key,
    command_id text not null references office.commands(command_id),
    runner_id text not null,
    status text not null default 'created',
    return_code integer,
    stdout_ref text,
    stderr_ref text,
    summary text not null default '',
    result_is_final boolean not null default false,
    chat_can_continue boolean not null default false,
    next_action text,
    started_at timestamptz,
    finished_at timestamptz
);

create table if not exists office.approvals (
    id text primary key,
    task_id text references office.tasks(id),
    command_id text references office.commands(command_id),
    risk_level text not null default 'low',
    approval_type text not null,
    requested_by text not null,
    approved_by text,
    status text not null default 'pending',
    reason text not null default '',
    created_at timestamptz not null default now(),
    decided_at timestamptz
);

create table if not exists office.artifacts (
    id text primary key,
    task_id text references office.tasks(id),
    command_id text references office.commands(command_id),
    type text not null,
    path text not null,
    title text not null default '',
    description text not null default '',
    checksum text,
    created_at timestamptz not null default now()
);

create table if not exists office.audit_events (
    id text primary key,
    event_type text not null,
    actor text not null,
    task_id text references office.tasks(id),
    command_id text references office.commands(command_id),
    payload_json jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create table if not exists office.local_runners (
    id text primary key,
    name text not null,
    base_url text not null,
    status text not null default 'unknown',
    capabilities jsonb not null default '[]'::jsonb,
    last_seen_at timestamptz,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists office_tasks_status_idx on office.tasks(status);
create index if not exists office_commands_status_idx on office.commands(status);
create index if not exists office_commands_target_chat_idx on office.commands(target_chat_id);
create index if not exists office_commands_delivery_kind_idx on office.commands(delivery_kind);
create index if not exists office_executions_command_id_idx on office.executions(command_id);
create index if not exists office_audit_events_created_idx on office.audit_events(created_at);
