# MerchantMiles — Loyalty Platform (in production)

## Overview

MerchantMiles is a loyalty platform designed to connect financial-card users with merchants, promotions and benefits. It is in production with the private banking divisions of **Clubmiles** and **Promerica**, across **Ecuador and Central America**.

The platform includes administrative capabilities for managing merchants, branches, users, benefits, campaigns, catalogues, data processing and reporting.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Roles

- **Technical Lead** — technical leadership, architecture, solution design, backend/frontend coordination and technical decision making.
- **Frontend Specialist** — frontend architecture, React/Next.js development and UI/UX implementation.

## Frontend

- React
- Next.js
- TypeScript
- TailwindCSS / component libraries
- Server/client rendering according to use case

## Backend

- .NET Core 8
- REST APIs
- Microservices
- PostgreSQL
- Docker

## Cloud

- AWS
- Object storage
- CDN
- Identity and access management
- Serverless components where appropriate
- Infrastructure as Code

## Engineering concerns

### Scalability

Services can scale independently according to business demand.

### Security

Authentication and authorization are enforced at the application boundary and service layer.

### Reliability

External integrations should use timeouts, retries where safe, circuit breakers and idempotency.

### Observability

Structured logs, metrics, health checks and trace correlation are required to diagnose distributed failures.

## Architectural lessons

- Define business boundaries before defining services.
- Avoid sharing databases indiscriminately.
- Keep external integrations isolated.
- Make asynchronous processing explicit.
- Document important decisions with ADRs.
