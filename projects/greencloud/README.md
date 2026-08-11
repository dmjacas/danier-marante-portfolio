# GreenCloud — Carbon Footprint SaaS (in production)

## Overview

**GreenCloud** is a SaaS tool for measuring the carbon footprint of organizations. It is used by companies including **Intel CR**, **Coca-Cola Bolivia**, **CAF** and **BCIE**.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Main capabilities

- Carbon footprint measurement and tracking
- Emissions reporting per scope and category
- Organization and facility management
- Data ingestion for emissions sources
- Dashboards and analytics
- Reporting for stakeholders and compliance

## Technologies

- SaaS multi-tenant platform
- Frontend (React/Next.js or component-based UI)
- Backend APIs
- PostgreSQL / relational database
- Reporting and export capabilities
- Secure role-based access

## Engineering concerns

### Multi-tenancy

Isolate organization data with clear tenancy boundaries.

### Performance

Handle emissions data volumes and reporting workloads reliably.

### Security

Protect organization emissions data and enforce access control.

### Report accuracy

Keep measurement logic deterministic and auditable.

### Observability

Logging and monitoring to diagnose production issues.

## Architectural lessons

- Model emissions domains clearly (scopes, categories, sources).
- Keep reporting deterministic for auditability.
- Isolate integrations behind contracts.
- Document important decisions with ADRs.