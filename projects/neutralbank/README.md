# NeutralBank — Environmental Impact Measurement for Multilateral Banking (in production)

## Overview

**NeutralBank** is a tool for measuring the environmental impact in **multilateral banking**, used in production to track and report on environmental metrics across banking operations and portfolios.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Main capabilities

- Environmental impact measurement
- Portfolio-level environmental tracking
- Metrics per operation and institution
- Reporting for stakeholders and compliance
- Dashboards and analytics

## Technologies

- SaaS / multi-tenant platform
- Frontend and backend APIs
- PostgreSQL / relational database
- Reporting and export capabilities
- Secure role-based access

## Engineering concerns

### Multi-tenancy

Isolate institution data with clear tenancy boundaries.

### Performance

Handle portfolio datasets and reporting workloads reliably.

### Security

Protect sensitive banking and environmental data.

### Reporting accuracy

Keep measurement logic deterministic and auditable.

### Observability

Logging and monitoring to diagnose production issues.

## Architectural lessons

- Model banking and environmental domains clearly.
- Keep reporting deterministic for auditability.
- Isolate integrations behind contracts.
- Document important decisions with ADRs.