# Scalability

## Context

Systems grow in users, data and processing volume. Scalability decisions must be tied to measurable demand, not speculation.

## Problem

Identify the bottlenecks that will constrain growth and choose the mechanisms — at the right layer — to absorb demand.

## Patterns

- **Stateless application tier:** scale horizontally behind a load balancer.
- **API Gateway:** centralized entry point, rate limiting, auth and routing.
- **Independent scaling of services:** each microservice scales by its own demand profile.
- **Database layer:** connection management, read replicas, caching (CDN/cache) before vertical scaling.
- **Asynchronous work:** queues/event-driven processing for bursts.
- **Serverless and managed services** where event-driven or bursty workloads justify it.

## Trade-offs

- Horizontal scaling adds deployment and consistency complexity.
- Caching improves latency but adds invalidation and consistency concerns.
- Managed services reduce operational burden but constrain control and can increase cost at scale.
- Premature scaling adds cost and complexity; scaling must follow measured demand.

## Consequences

- Performance is measured instead of guessed (principles: measurable performance).
- Observability must reveal the critical paths and bottlenecks.
- Load and capacity testing validate the design before it matters in production.

## Related

- [Microservices](microservices.md)
- [Cloud Architecture](cloud-architecture.md)
- [Distributed Systems](distributed-systems.md)