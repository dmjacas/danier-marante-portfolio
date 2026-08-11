# MerchantMiles — Loyalty Platform (Fintech / Banking)

## Executive Summary

MerchantMiles is a loyalty platform that connects financial-card users with merchants, promotions and benefits. It is **in production** with the private banking divisions of **Clubmiles** and **Promerica**, across **Ecuador and Central America**.

For the private banking client it works as a benefits ecosystem that encourages card usage; for merchants it is a channel to launch campaigns and benefits; for platform administrators it provides tools to manage merchants, branches, users, benefits, campaigns, catalogues, data processing and reporting.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Business Problem

Banks need their private-banking clients to perceive real value from their cards beyond payments. Without a structured benefits ecosystem, banks cannot easily connect their clients with relevant merchants and offers, and merchants cannot reach a qualified premium audience.

**Problem:** How to deliver a scalable loyalty ecosystem that lets banks run benefits and campaigns for private clients — across multiple countries — while keeping the platform reliable, secure and operationally manageable.

## Solution

A multi-tenant loyalty platform composed of:

- A **customer-facing and administration web application** for benefits, campaigns and catalogue management.
- **Backend services** organized around business capabilities (users, benefits, campaigns, merchants) with explicit API contracts.
- An **AWS cloud footprint** with Infrastructure as Code, managed storage, CDN, identity and access management, and serverless components where appropriate.
- **PostgreSQL** as the transactional data platform.

## My Role

### Leadership

- Technical leadership of the digital product
- Solution design and technical decision making
- Backend/frontend coordination
- Code quality and CI/CD/deployment coordination

### Architecture

- Frontend architecture (React, Next.js, TypeScript)
- Backend architecture (microservices, .NET Core 8)
- Cloud architecture (AWS) and Infrastructure as Code

### Engineering / Frontend Specialist

- Frontend development and UI/UX implementation
- API integration and server/client rendering decisions
- Quality, observability and delivery support

## Architecture

```text
                         ┌─────────────────────┐
                         │      Clients        │
                         │ React / Next.js     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      API Layer      │
                         └──────────┬──────────┘
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
          ┌──────────┐        ┌──────────┐        ┌──────────┐
          │  Users   │        │ Benefits │        │Campaigns │
          │ Service  │        │ Service  │        │ Service  │
          └────┬─────┘        └────┬─────┘        └────┬─────┘
               │                   │                   │
               └───────────────────┼───────────────────┘
                                   ▼
                              PostgreSQL

                    AWS / Docker / CI-CD / IaC
```

## Technology Stack

- React, Next.js, TypeScript, TailwindCSS / component libraries
- .NET Core 8, REST APIs, microservices
- PostgreSQL
- AWS (object storage, CDN, IAM, serverless where appropriate), Docker
- Infrastructure as Code, CI/CD

## Architecture Decisions

### Why microservices?

**Context:** Multiple business capabilities (users, benefits, campaigns, merchants, reporting) with different scaling and ownership requirements across countries.

**Options:**
1. Monolith
2. Modular monolith
3. Microservices

**Decision:** Services around meaningful business capabilities (microservices), because independent ownership, deployment and scaling were required for a multi-country product.

**Rationale:** The platform spans several banks and countries; capabilities evolve at different rates and must scale independently.

**Trade-offs:**
- *Benefits:* independent deployment/scaling, clear ownership, reduced coupling.
- *Costs:* distributed-system complexity, network failures, operational and observability overhead.

## Challenges

| Area | Challenge | Outcome |
|---|---|---|
| Scalability | Demand peaks around campaigns require services to scale independently | Microservices design with independent scaling |
| Security | Authentication/authorization for multi-tenant private-banking data | Enforcement at application boundary and service layer |
| Integration | Multiple external financial/commerce integrations | Isolated integrations with timeouts, retries where safe, circuit breakers, idempotency |
| Observability | Diagnosing failures across distributed services | Structured logs, metrics, health checks, trace correlation |
| Deployment | Coordinate backend/frontend releases | CI/CD and deployment coordination under technical lead scope |

## Trade-offs

- **Microservices vs Monolith:** chosen microservices for independent scaling and ownership; accepted operational complexity.
- **Managed services vs self-managed infrastructure:** preferred AWS managed services to reduce operational burden; kept Infrastructure as Code for reproducibility.
- **Server/client rendering:** chosen per use case — SEO/initial-load paths server-rendered, interactive admin panels client-rendered.
- **Relational database as primary store:** PostgreSQL for transactional consistency; SQL/migrations maturity over NoSQL.

## Engineering Concerns

### Scalability

Services can scale independently according to business demand.

### Security

Authentication and authorization are enforced at the application boundary and service layer.

### Reliability

External integrations use timeouts, retries where safe, circuit breakers and idempotency.

### Observability

Structured logs, metrics, health checks and trace correlation are required to diagnose distributed failures.

## Results

- Loyalty platform **in production** with private banking divisions of **Clubmiles** and **Promerica** in **Ecuador and Central America**.

> Quantitative impact metrics (users, transactions, campaigns, availability) are `[Metric to validate]` and are only included once confirmed.

## Lessons Learned

- Define business boundaries before defining services.
- Avoid sharing databases indiscriminately.
- Keep external integrations isolated.
- Make asynchronous processing explicit.
- Document important decisions with ADRs.
- Frontend architecture and UI/UX quality are decisive for adoption of client-facing loyalty products.

---

## Related

- [PPM Publipromueve experience →](../../experience/ppm.md)
- [Architecture decision: Microservices →](../../docs/architecture-decisions/ADR-001-microservices.md)
- [Architecture decision: PostgreSQL →](../../docs/architecture-decisions/ADR-002-postgresql.md)
- [Architecture decision: AWS →](../../docs/architecture-decisions/ADR-003-aws.md)