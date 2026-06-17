from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOCS=[
    ROOT/'docs'/'research'/'WS_AI_OFFICE_PHASE_C_READONLY_SMOKE_DESIGN_2026-06-17.md',
    ROOT/'docs'/'obsidian'/'Research'/'Phase_C_Readonly_Smoke_Design.md',
]

REQUIRED=[
    'documentation only',
    'readonly smoke design',
    'database_enabled=false',
    'execution_enabled=false',
    'local_runner_enabled=false',
    'gateway_integration_enabled=false',
    'no runtime gateway integration',
    'no live polling',
    'no real claim',
    'no real ack',
    'ACK posting remains disabled',
]

BLOCKED=[
    'no GET /bridge/next-action call',
    'no POST /bridge/events call',
    'no POST /bridge/acks call',
    'no GET /claim call',
    'no POST /ack call',
    'no run-command execution',
    'no send-chat-message execution',
    'no db-query',
    'no file-ops',
    'no codex-analyze',
    'no production queue read',
]

for doc in DOCS:
    if not doc.exists():
        raise AssertionError(f'missing doc: {doc}')
    text=doc.read_text(encoding='utf-8')
    for item in REQUIRED+BLOCKED:
        if item not in text:
            raise AssertionError(f'missing {item} in {doc}')

# Contract-only safety: the smoke must not import app, call network, or mutate state.
print('SMOKE_PHASE_C_READONLY_DESIGN_DOCS_OK')
