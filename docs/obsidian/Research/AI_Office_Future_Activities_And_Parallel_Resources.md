# AI Office Future Activities and Parallel Resources

Date: 2026-06-18
Status: roadmap documentation only. No route creation. No database change. No migration. No runtime gateway integration.

## Purpose

This document consolidates future AI Office activities and parallel resources that will be added while the Pizza App integration remains docs-only, smoke-only and readonly.

## Product vision

AI Office is a virtual AI manager. Pizza App continues to execute restaurant operation and remains the source of truth.

Expected final product support:

- operational summaries
- alert and risk explanations
- recommendation drafts
- daily virtual manager briefings
- controlled future action proposals
- auditability and approval gates
- no unapproved mutation of operational systems

## Repository responsibilities

### AI Office repository

Path: `D:/dev/autocode/ai-office`

Use for product vision, AI Office-side contracts, recommendation planning, snapshot consumption planning, UI/manager workflow planning, security matrix, docs and smokes.

### Pizza App repository

Path: `D:/dev/pizza`

Use for Pizza App-side readonly discovery, readonly API contract draft, future implementation checklist, Pizza-owned snapshot design, docs and smokes.

### AI Bridge Local repository

Path: `D:/dev/autocode/ai-bridge-local`

Use only for watcher protocol, envelope handling, queued/final result behavior, delivery diagnostics, bridge safety and local orchestration docs.

## Immediate gate

Do not start Micro42 until Micro41 returns a final result:

- `AI_LOCAL_RUN`
- `result_is_final=1`
- either `success=1` or `success=0`

If Micro41 succeeds, summarize files, smoke marker, commit and push.
If Micro41 fails, analyze stdout/stderr and create a safe correction with a new command_id.

## Planned micros after Micro41

### Micro42 - Pizza readonly implementation checklist

Repository: `D:/dev/pizza`
Mode: docs-only and smoke-only.

Goal: document all preconditions for a future Pizza App readonly implementation without creating routes.

Required topics:

- authentication
- authorization
- tenant isolation
- business isolation
- data minimization
- snapshot behavior
- audit logging
- rate limits
- pagination
- result-size limits
- timeout behavior
- staging/test environment first
- rollback plan
- no operational mutations

Forbidden in Micro42:

- route creation
- database schema changes
- migrations
- direct database reads
- production queue reads
- payment capture
- refund
- campaign sending
- coupon creation
- customer message sending
- menu mutation
- order mutation
- delivery status changes

### Micro43 - AI Office contract alignment

Repository: `D:/dev/autocode/ai-office`
Mode: docs-only and smoke-only.

Goal: align AI Office docs with the Pizza App-side readonly API contract created in Micro41.

### Micro44 - Pizza docs smoke consolidation

Repository: `D:/dev/pizza`
Mode: docs-only and smoke-only.

Goal: add or update a consolidated smoke covering readonly discovery docs, readonly API contract draft and readonly implementation checklist.

### Micro45 - AI Office snapshot consumption plan

Repository: `D:/dev/autocode/ai-office`
Mode: docs-only and smoke-only.

Goal: plan how AI Office will consume future approved Pizza App snapshots.

### Micro46 - Pizza snapshot design draft

Repository: `D:/dev/pizza`
Mode: docs-only and smoke-only.

Goal: design Pizza-owned readonly snapshot formats for future exposure.

### Micro47 - Security and authorization matrix

Repository: `D:/dev/autocode/ai-office`
Mode: docs-only and smoke-only.

Goal: document security boundaries across AI Office, Pizza App and watcher.

### Micro48 - Staging rollout plan

Repository: `D:/dev/pizza`
Mode: docs-only and smoke-only.

Goal: plan how a future readonly implementation would be tested in staging before production.

## Parallel resources to add

### Product resources

- product vision brief
- restaurant owner daily briefing template
- AI Office recommendation categories
- AI Office alert categories
- AI Office decision log template
- AI Office virtual manager workflow map

### Integration resources

- readonly snapshot vocabulary
- readonly response shape examples
- data freshness policy
- stale snapshot handling policy
- result-size limit policy
- retry and timeout policy
- consumer/provider responsibility matrix

### Safety resources

- no-mutation checklist
- forbidden actions matrix
- tenant isolation checklist
- personal data minimization checklist
- audit log field list
- approval gate matrix
- rollback checklist
- staging-first checklist

### Smoke resources

- docs smoke for every new planning document
- consolidated docs smoke per phase
- marker-based validation for forbidden actions
- marker-based validation for repository ownership
- marker-based validation for docs-only status

## Required validation pattern

Every docs micro should follow this pattern:

1. `git status -sb`
2. stop if repo is not clean/aligned
3. create or update exact docs
4. create or update exact smoke
5. run `python -m py_compile <smoke>`
6. run the smoke
7. run relevant existing smokes
8. `git add --intent-to-add -- <exact paths>`
9. `git diff --check`
10. `git reset -- <exact paths>`
11. `git add -- <exact paths>`
12. `git diff --cached --check`
13. `git diff --cached --stat`
14. commit with a focused message
15. push
16. final `git status -sb`

## Mandatory safety limits

- docs-only
- smoke-only
- readonly
- no route creation
- no database change
- no migration
- no direct database query
- no runtime gateway integration
- no production queue read
- no live polling
- no real claim
- no real ack
- no payment capture
- no refund
- no coupon creation
- no campaign sending
- no menu mutation
- no customer message sending
- no order mutation
- no delivery status change
- no stock mutation
- no supplier mutation
- no app-runtime command execution
- no app-runtime send-chat-message
- no git add dot

## Decision rule for leaving docs-only

Leaving docs-only requires explicit approval after:

- Micro41 final success
- Micro42 checklist success
- AI Office alignment docs success
- security matrix success
- staging/test plan success
- clear rollback and audit plan
