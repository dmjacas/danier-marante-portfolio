# Microservices Architecture

## Experience

Applied in production in the MerchantMiles loyalty platform: backend services organized around business capabilities (users, benefits, campaigns, merchants, reporting) behind an API Gateway, with independent deployment and scaling.

## Philosophy

Microservices should be introduced when independent business capabilities, deployment requirements, scaling characteristics or team boundaries justify the additional operational complexity.

## Problems Encountered

- Multi-country product with capabilities evolving at different rates and demand profiles.
- Orchestrating backend/frontend coordination with independent releases.
- Diagnosing distributed failures across services.

## Reference Architecture

```text
                         ┌───────────────────┐
                         │   Web / Mobile    │
                         └─────────┬─────────┘
                                   │ HTTPS
                                   ▼
                         ┌───────────────────┐
                         │    API Gateway    │
                         └─────────┬─────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
       ┌────────────┐       ┌────────────┐       ┌────────────┐
       │   Users    │       │  Benefits  │       │ Campaigns  │
       │  Service   │       │  Service   │       │  Service   │
       └─────┬──────┘       └─────┬──────┘       └─────┬──────┘
             │                    │                    │
             ▼                    ▼                    ▼
       PostgreSQL            PostgreSQL            PostgreSQL
```

## Design principles

- Business capability boundaries
- Explicit API contracts
- Independent deployment
- Stateless services where possible
- Centralized authentication
- Distributed tracing
- Structured logging
- Health checks
- Resilience and timeouts
- Database ownership by service

## Common trade-offs

Microservices provide independent scalability and deployment, but introduce distributed-system complexity, network failures, observability requirements and operational overhead.

The architecture should therefore be justified by business and organizational requirements rather than technology preference.

## Lessons Learned

- Define business boundaries before defining services.
- Avoid sharing databases indiscriminately.
- Make asynchronous processing explicit.
- Treat observability as a design requirement, not an afterthought.
- Document decisions as ADRs.

## Related

- [MerchantMiles case study →](../projects/merchant-miles/README.md)
- [ADR-001 — Microservices →](../docs/architecture-decisions/ADR-001-microservices.md)
- [Availability & Reliability](availability.md)
- [Distributed Systems](distributed-systems.md)
