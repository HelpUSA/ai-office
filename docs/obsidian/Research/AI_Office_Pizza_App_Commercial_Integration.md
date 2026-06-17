# AI Office + Pizza App - Commercial Integration Research

Date: 2026-06-17
Status: documentation only. No runtime gateway integration.

## Purpose

Document the practical commercial vision for using AI Office together with the Pizza App project. The Pizza App remains the operational restaurant system for menu, orders, payments, delivery, cash flow and finance. AI Office becomes the intelligent operational layer that explains, recommends, assists, audits and later automates approved routines.

## Core idea

Pizza App is the system that executes the restaurant operation. AI Office is the intelligent office layer that understands the operation, helps humans make decisions, suggests safe actions and coordinates AI agents with auditability.

In commercial terms, the combined product is not only a digital ordering system. It becomes an AI-powered restaurant operating platform.

## Pizza App responsibilities

- Digital menu and item management.
- Customer orders.
- Payment status and payment methods.
- Delivery flow and order status.
- Cash register and financial records.
- Product, category and promotion management.
- Customer records and order history.
- Operational reporting.

## AI Office responsibilities

- Conversational customer assistance.
- Order interpretation and structured handoff to Pizza App.
- Daily business summaries.
- Operational alerts.
- Financial explanations.
- Marketing suggestions.
- Customer recovery suggestions.
- Stock and demand insights.
- Human approval workflows.
- Audit logs and safe automation governance.

## Practical customer flow

1. A customer sends a message through WhatsApp, website, Instagram or app.
2. AI Office understands the request and asks missing questions.
3. Pizza App receives the structured order.
4. Pizza App calculates price, delivery fee, payment status and preparation queue.
5. AI Office confirms the order in natural language.
6. Pizza App sends the order to kitchen and delivery workflow.
7. AI Office monitors delays, questions and customer satisfaction.
8. Sensitive actions remain gated by human approval.

## Example: customer order

Customer: I want a large calabresa pizza and a Coke.

AI Office can ask for address, confirm size, suggest add-ons, identify returning customers and prepare a structured order. Pizza App registers and executes the order. AI Office explains the status and escalates to a human if there is uncertainty or risk.

## Example: owner asks about yesterday

Owner: How was yesterday?

AI Office can answer from Pizza App data: number of orders, revenue, average ticket, best-selling items, cancellations, delivery delays, payment mix and operational bottlenecks. It can also suggest actions such as adding one delivery driver during peak hours or creating a combo for a best-selling item.

## Commercial value

The customer buys more than software for orders. The customer buys a virtual AI manager for the restaurant operation. The value proposition is faster service, higher average ticket, fewer missed opportunities, better financial visibility, better customer recovery and safer automation.

## Commercial positioning

Suggested positioning: AI-powered restaurant operating platform.

Alternative positioning: Pizza App handles the operation. AI Office becomes the AI manager that attends, analyzes, suggests, alerts and automates safely.

## Possible product plans

### Basic plan

- Pizza App traditional features.
- Digital menu.
- Orders.
- Payments.
- Delivery flow.
- Basic reports.

### Pro plan with AI Office

- AI customer assistant.
- Daily AI summary.
- Operational alerts.
- Smart reports.
- Suggestions for campaigns and combos.
- Customer recovery suggestions.

### Premium plan

- Controlled automations with approval.
- Stock and demand forecasting.
- Campaign segmentation.
- Financial insights.
- Real-time operational assistant.
- AI-driven customer follow-up.

## Integration phases

### Phase 1 - readonly

AI Office only reads Pizza App data. No execution. No mutation. Safe outputs include daily summaries, natural-language questions, alerts and reports.

### Phase 2 - suggestions

AI Office suggests actions such as campaigns, discounts, stock purchases, menu adjustments, customer replies and operational corrections. Humans approve.

### Phase 3 - controlled execution

AI Office can execute low-risk approved actions such as sending status messages, generating small coupons within limits, sending post-sale surveys or generating daily reports. Sensitive actions remain approval-only.

### Phase 4 - virtual manager

AI Office monitors the operation, detects bottlenecks, recommends decisions, executes approved routines and learns safe patterns for each restaurant.

## Safety and governance

- documentation only
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

## Runtime behaviors still forbidden

- no GET /bridge/next-action call
- no POST /bridge/events call
- no POST /bridge/acks call
- no GET /claim call
- no POST /ack call
- no run-command execution from app runtime
- no send-chat-message execution from app runtime
- no db-query
- no file-ops
- no codex-analyze
- no production queue read

## Future research topics

- Define the minimum readonly API contract between Pizza App and AI Office.
- Define customer support assistant boundaries.
- Define order handoff schema.
- Define manager dashboard cards.
- Define approval rules for coupons, cancellations, refunds and campaigns.
- Define finance summary fields.
- Define restaurant-specific AI agents.
- Define pilot pricing and packaging.

## Recommended next safe micro

Create a docs-only smoke that protects this commercial integration research and its safety markers.
