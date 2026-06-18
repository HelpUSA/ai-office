# AI Office + Pizza App - Commercial Plan Matrix

Date: 2026-06-18
Status: documentation only. No runtime gateway integration.

## Purpose

Define a commercial plan matrix for packaging the future Pizza App and AI Office product without enabling runtime execution. This matrix is commercial research only and does not implement billing, feature flags, payments, access control, tenant provisioning, gateway operations, queue reads or database access.

## Product positioning

The combined product is an AI-powered restaurant operating platform. Pizza App remains the source of truth for orders, menu, customers, delivery, payments and finance. AI Office is the intelligent office layer that explains data, summarizes operations, drafts suggestions and helps the owner decide what to do next.

## Safety baseline for every plan

Every plan in this draft keeps the same safety boundary:

- documentation only
- commercial plan matrix
- commercial research only
- Pizza App remains the source of truth
- AI Office remains advisory unless a future approved implementation changes that boundary
- no runtime gateway integration
- database_enabled=false
- execution_enabled=false
- local_runner_enabled=false
- gateway_integration_enabled=false
- no live polling
- no real claim
- no real ack
- ACK posting remains disabled
- no production queue read
- no direct database query by AI Office
- no command execution from app runtime
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no db-query
- no file-ops
- no codex-analyze
- no mutation of orders
- no delivery status change
- no payment capture
- no refund
- no coupon creation
- no campaign sending
- no menu price change
- no menu availability change
- no customer message sending
- no customer data export
- no stock mutation
- no supplier order creation

## Plan 1 - Basic

### Target customer

Small restaurant, single store, owner-operator, wants visibility and simple daily summaries.

### Positioning

Basic is the reporting and clarity plan.

### Included capabilities

- Daily operations summary
- Orders summary
- Revenue summary
- Menu performance summary
- Delayed order visibility
- Basic customer activity summary
- End-of-day explanation
- Readonly operational snapshots
- Manual review by owner

### Excluded capabilities

- suggestion workflow
- campaign drafting
- customer follow-up drafts
- promotion suggestions
- multi-store reporting
- approval workflow
- virtual manager routines

### Safety posture

Basic is readonly only. AI Office may read approved operational snapshots but must not create suggestions that look like approved actions.

## Plan 2 - Pro

### Target customer

Growing restaurant with recurring operations, delivery flow and marketing needs.

### Positioning

Pro is the insights and suggestions plan.

### Included capabilities

- Everything in Basic
- Suggestion Contract support
- delayed order attention suggestions
- promotion idea suggestions
- menu review suggestions
- customer follow-up draft suggestions
- stock and purchasing attention suggestions
- finance review suggestions
- human approval required
- requires_human_approval: true
- execution_allowed: false
- approval_status: draft

### Excluded capabilities

- automatic coupon creation
- automatic campaign sending
- automatic refunds
- automatic customer messaging
- automatic menu changes
- automatic stock changes

### Safety posture

Pro is suggestion only. AI Office may generate recommendations, but every recommendation remains a draft until a human reviews it.

## Plan 3 - Premium

### Target customer

Restaurant owner who wants a virtual manager experience with more structured routines and stronger operational guidance.

### Positioning

Premium is the virtual manager with approval workflow plan.

### Included capabilities

- Everything in Pro
- virtual manager daily briefing
- weekly owner summary
- recurring operational checklists
- approval queue concept
- suggestion priority ranking
- risk level per suggestion
- suggested action drafts
- owner decision history concept
- audit notes concept

### Excluded capabilities

- autonomous execution
- direct payment actions
- direct production queue actions
- direct database access
- direct local runner actions
- automatic operational changes

### Safety posture

Premium may describe virtual manager behavior, but this document does not permit execution. Human approval remains required and execution remains disabled.

## Plan 4 - Enterprise

### Target customer

Multi-store operator, franchise, restaurant group or agency managing restaurants.

### Positioning

Enterprise is the governance and multi-location plan.

### Included capabilities

- Everything in Premium
- multi-store reporting concept
- franchise level dashboard concept
- brand-level menu insights concept
- cross-store performance comparison concept
- role-based approval concept
- audit export concept
- compliance review concept
- tenant governance concept

### Excluded capabilities

- real tenant provisioning
- real billing implementation
- real role enforcement
- real audit export
- real multi-store database connection
- real gateway integration

### Safety posture

Enterprise remains documentation only. Multi-store and tenant capabilities are product concepts, not implementation permissions.

## Packaging table

| Capability | Basic | Pro | Premium | Enterprise |
| --- | --- | --- | --- | --- |
| Daily summary | yes | yes | yes | yes |
| Readonly dashboards | yes | yes | yes | yes |
| Suggestion Contract | no | yes | yes | yes |
| Customer follow-up drafts | no | yes | yes | yes |
| Promotion idea suggestions | no | yes | yes | yes |
| Virtual manager briefing | no | no | yes | yes |
| Approval queue concept | no | no | yes | yes |
| Multi-store concept | no | no | no | yes |
| Franchise governance concept | no | no | no | yes |
| Runtime execution | no | no | no | no |

## Pricing research placeholders

This draft intentionally does not set final prices. Possible pricing research bands:

- Basic: low monthly SaaS entry plan
- Pro: medium monthly SaaS plan
- Premium: higher monthly SaaS plan for owner-operator automation guidance
- Enterprise: custom pricing for multi-store operations

These are research placeholders only, not billing implementation.

## Recommended next safe micro

After this matrix is protected by a smoke, the next safe activity is to document a Phase 1 integration readiness checklist for the Pizza App repository before any code integration work.
