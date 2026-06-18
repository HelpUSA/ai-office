# AI Office + Pizza App - Readonly API Contract Draft

Date: 2026-06-17
Status: documentation only. No runtime gateway integration.

## Purpose

Define the minimum readonly API contract that Pizza App could expose to AI Office in a future integration. This draft is documentation only and does not approve implementation, live polling, database access, runtime gateway integration, command execution or production queue access.

## Core principle

Pizza App remains the source of truth for restaurant operations. AI Office may read approved operational snapshots and generate summaries, alerts, recommendations and human-review suggestions. AI Office must not mutate Pizza App state in the readonly phase.

## Phase 1 readonly objective

The first integration phase should allow AI Office to answer operational questions without changing data. Example questions include: how many orders happened today, which items sold most, which orders are delayed, what is the payment mix, what customers are inactive and what operational risks should the owner review.

## Readonly data domains

### Orders

- order_id
- created_at
- status
- channel
- customer_id
- customer_name_display
- items_summary
- total_amount
- payment_method
- payment_status
- delivery_type
- delivery_neighborhood
- estimated_delivery_at
- completed_at
- canceled_at
- cancellation_reason

### Menu

- item_id
- category_id
- item_name
- category_name
- active
- base_price
- option_summary
- availability_status

### Customers

- customer_id
- display_name
- phone_masked
- last_order_at
- order_count
- total_spent
- favorite_items_summary
- marketing_opt_in

### Delivery

- order_id
- delivery_status
- neighborhood
- driver_name_display
- estimated_delivery_at
- departed_at
- delivered_at
- delay_minutes

### Finance summary

- business_date
- gross_revenue
- net_revenue_estimate
- order_count
- average_ticket
- payment_method_breakdown
- refunds_count
- refunds_amount
- discounts_amount
- delivery_fee_total

### Operational alerts

- delayed_orders_count
- canceled_orders_count
- unavailable_items_count
- payment_failures_count
- customer_complaints_count
- stock_attention_summary

## Suggested readonly endpoints

These endpoints are examples for future design only. They are not implemented here.

- GET /ai-office/readonly/health
- GET /ai-office/readonly/orders/summary
- GET /ai-office/readonly/orders/recent
- GET /ai-office/readonly/orders/delayed
- GET /ai-office/readonly/menu/summary
- GET /ai-office/readonly/customers/summary
- GET /ai-office/readonly/customers/inactive
- GET /ai-office/readonly/delivery/summary
- GET /ai-office/readonly/finance/daily-summary
- GET /ai-office/readonly/alerts/summary

## Response envelope draft

A future readonly response should include:

- schema_version
- source_system: Pizza App
- generated_at
- business_id
- data_scope
- readonly: true
- records
- summary
- warnings
- pagination when needed

## Example safe response

The AI Office should receive business data snapshots, not direct database handles. Sensitive fields should be masked when not required. Customer phone numbers should be masked by default unless a specific approved communication workflow requires otherwise in a later phase.

## Forbidden in readonly phase

- no mutation of orders
- no payment capture
- no refund
- no coupon creation
- no campaign sending
- no menu price change
- no customer data export
- no production queue read
- no direct database query by AI Office
- no command execution from app runtime
- no live gateway polling

## Approval boundaries for later phases

Later phases may propose actions, but the readonly contract must remain separate from write actions. Cancellations, refunds, coupons, price changes, customer messages and campaigns require explicit approval rules before implementation.

## Safety and governance markers

- documentation only
- readonly API contract draft
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

Create a docs-only smoke that protects this readonly API contract draft and its safety markers.
