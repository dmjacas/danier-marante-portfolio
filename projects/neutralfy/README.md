# Neutralfy — Carbon Footprint Compensation for Air Travel (in production)

## Overview

**Neutralfy** is a tool for compensating the carbon footprint of **air travel**, used in production to help individuals and organizations offset the emissions of their flights.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Main capabilities

- Flight carbon footprint calculation
- Offsetting / compensation flows
- User accounts and payment integration
- Organization and individual usage
- Reporting and analytics
- Certificates / proofs of compensation

## Technologies

- SaaS platform
- Frontend and backend APIs
- PostgreSQL / relational database
- Payment integration
- Aviation/emissions calculation logic
- Secure role-based access

## Engineering concerns

### Calculation accuracy

Keep emissions and compensation math deterministic and auditable.

### Payments

Secure and idempotent payment handling for compensation purchases.

### Performance

Fast responses for flight calculations and checkout.

### Security

Protect user data and payment information.

### Observability

Logging and monitoring to diagnose production issues.

## Architectural lessons

- Keep calculation rules explicit and auditable.
- Isolate payment integrations behind contracts.
- Track compensation states explicitly.
- Document important decisions with ADRs.