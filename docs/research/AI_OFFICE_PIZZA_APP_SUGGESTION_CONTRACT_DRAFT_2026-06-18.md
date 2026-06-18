# AI Office + Pizza App - Suggestion Contract Draft

Date: 2026-06-18
Status: documentation only. No runtime gateway integration.

## Purpose

Define a safe suggestion-only contract for a future Pizza App and AI Office integration. This contract describes what AI Office may recommend to a human operator after reading approved Pizza App snapshots. It does not approve implementation, mutation, payment actions, campaign sending, live polling, database access, runtime gateway integration, command execution or production queue access.

## Core principle

Pizza App remains the source of truth for restaurant operations. AI Office may generate suggestions, explanations, alerts and draft actions, but every action remains human approval required. The system is suggestion only until a later explicit implementation phase defines guarded write permissions.

## Relationship with readonly contract

The readonly API contract gives AI Office safe visibility into operational snapshots. This suggestion contract sits on top of that readonly information and converts insights into human-review proposals. The suggestion contract must not bypass the readonly boundary.

## Suggestion envelope

Every future suggestion should include:

- suggestion_id
- schema_version
- source_system: AI Office
- target_system: Pizza App
- generated_at
- business_id
- suggestion_type
- priority
- reason
- evidence_summary
- proposed_action
- expected_benefit
- risk_level
- requires_human_approval: true
- execution_allowed: false
- approval_status: draft
- expires_at
- audit_notes

## Allowed suggestion types

### Delayed order attention

AI Office may suggest that a human operator review delayed orders. It may explain which orders appear delayed, why the risk matters and what response could be considered. It must not cancel, refund, message the customer or change delivery status.

### Promotion idea

AI Office may suggest a promotion based on slow periods, low-selling products or customer history. It must not create coupons, change prices, publish campaigns or send customer messages.

### Menu review

AI Office may suggest that the owner review inactive items, unavailable products, confusing option groups or high-cancellation items. It must not change menu items, prices, categories, availability or images.

### Customer follow-up draft

AI Office may draft a suggested message for a customer follow-up after a complaint, cancellation or long inactivity. It must not send the message. A human must review and approve any communication.

### Stock and purchasing attention

AI Office may suggest that the operator check stock or purchasing needs based on sales patterns. It must not place purchase orders, alter stock counts or create supplier commitments.

### Finance review

AI Office may suggest that the owner review unusual payment mix, refunds, discounts, low average ticket or revenue drops. It must not capture payments, issue refunds, alter cash register records or export customer data.

## Forbidden actions

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
- no production queue read
- no direct database query by AI Office
- no command execution from app runtime
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no live gateway polling
- no runtime gateway integration

## Approval states

A suggestion can only move through documentation-defined conceptual states:

- draft
- presented_to_human
- approved_by_human
- rejected_by_human
- expired
- archived

This document does not implement approval state changes. It only defines the future vocabulary.

## Safety and governance markers

- documentation only
- suggestion contract draft
- suggestion only
- human approval required
- requires_human_approval: true
- execution_allowed: false
- approval_status: draft
- commercial research only
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
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no db-query
- no file-ops
- no codex-analyze

## Recommended next safe micro

After this document is protected by a smoke, the next safe step is to document the commercial plan matrix for Basic, Pro, Premium and Enterprise packages.
