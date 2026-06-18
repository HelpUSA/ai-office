# AI Office Project Index

Date: 2026-06-18
Status: documentation index only. No runtime gateway integration.

## Product summary

AI Office is a virtual office and virtual AI manager for business operations. In the current track it is being prepared to work with Pizza App. Pizza App remains the operational source of truth. AI Office may later consume approved readonly snapshots, explain what is happening, summarize risks, draft recommendations and prepare controlled action proposals after explicit approval.

## Current phase

- docs-only
- smoke-only
- readonly
- no route creation
- no database change
- no migration
- no direct database query
- no runtime gateway integration
- no production queue read
- no app-runtime command execution
- no operational mutation

## Main repositories

- AI Office: `D:/dev/autocode/ai-office`
- Pizza App: `D:/dev/pizza`
- AI Bridge Local / watcher: `D:/dev/autocode/ai-bridge-local`

## Completed AI Office track

- Commercial AI Office + Pizza App research docs and smoke.
- AI Office-side readonly API contract draft and smoke.
- AI Office-side suggestion contract draft and smoke.
- Commercial plan matrix docs and smoke.
- Phase 1 integration readiness checklist docs and smoke.
- Latest known AI Office commit: `eab4254 docs: add pizza phase1 readiness checklist`.

## Completed Pizza App track

- Pizza App readonly discovery docs and smoke.
- Latest known Pizza commit: `37ac4c5 docs: add ai office readonly discovery`.
- Micro41 pending/active until its final AI_LOCAL_RUN is received.

## Future planning docs

- `docs/research/AI_OFFICE_FUTURE_ACTIVITIES_AND_PARALLEL_RESOURCES_2026-06-18.md`
- `docs/obsidian/Research/AI_Office_Future_Activities_And_Parallel_Resources.md`

## Operating rule

Do not start implementation work until the current docs-only, smoke-only and readonly phase is explicitly approved to move forward.
