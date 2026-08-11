# Distributed Systems

## Context

Multi-service and multi-node systems address business requirements for independent scaling, ownership and availability. Distributed systems also introduce hard problems that a monolith does not have.

## Problem

Design, operate and troubleshoot systems made of multiple components communicating over a network, where partial failure is an expected state.

## Principles

- **Design for failure:** assume any remote call can fail; use timeouts, retries where safe, circuit breakers and bulkheads.
- **Idempotency:** repeated operations must be safe; client-issued idempotency keys for high-value flows (payments, orders).
- **Consistency model:** choose strongly consistent paths for transaction-critical data and eventual consistency elsewhere.
- **Observability:** distributed tracing, structured logs and metrics are mandatory to explain failures across components.
- **Contract first:** services communicate through explicit, versioned API contracts.

## Trade-offs

- Distributed systems provide independent scaling and deployment but increase operational and debugging complexity.
- Strong consistency is safer but costs availability/latency; eventual consistency is faster but requires reconciliation.
- Event-driven decoupling improves resilience and scaling but makes causality and debugging harder to reason about.

## Consequences

- Centralized authentication and API gateway shape the boundaries.
- Every service owns its data; shared databases are avoided.
- Deployment, monitoring and incident response tooling become first-class concerns.

## Related

- [Microservices](microservices.md)
- [Event-Driven](event-driven.md)
- [Scalability](scalability.md)
- [Observability as an engineering concern](../projects/merchant-miles/README.md)