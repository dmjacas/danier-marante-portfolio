# ADR-001 — Microservices

## Status

Accepted

## Context

Some business capabilities require independent ownership, deployment and scaling. In products such as MerchantMiles, capabilities (users, benefits, campaigns, merchants, reporting) evolve at different rates and face different demand profiles across countries.

## Problem

How to organize a multi-capability, multi-country product so that each capability can be developed, deployed and scaled independently without creating unmanageable coupling.

## Options Considered

### Option 1 — Monolith

A single deployable application with shared database.

- Pros: simple, fast to start, no distributed complexity.
- Cons: cannot scale capabilities independently; deployment couples every change; ownership is blurred as the team grows.

### Option 2 — Modular Monolith

A single deployable with strong internal module boundaries.

- Pros: simpler operations, explicit boundaries.
- Cons: does not allow independent scaling or deployment of a single capability.

### Option 3 — Microservices

Services around business capabilities with explicit API contracts.

- Pros: independent deployment, scaling and ownership.
- Cons: distributed-system complexity, network failures, operational and observability overhead.

## Decision

Use service-oriented boundaries around meaningful business capabilities rather than creating services purely around technical layers. Adopt microservices where independent ownership, deployment and scaling are required.

## Rationale

The product spans several banks and countries; capabilities have different scaling and release requirements. Business capability boundaries provide the natural seams for ownership and evolution.

## Trade-offs

### Advantages

- Independent deployment
- Independent scaling
- Clear ownership
- Reduced coupling

### Disadvantages

- Distributed-system complexity
- Network failures
- More operational tooling
- Higher observability requirements

## Consequences

- API contracts must be explicit and versioned.
- Each service owns its data; shared databases are avoided.
- Observability (tracing, logs, metrics), CI/CD and deployment tooling become first-class concerns.

## Related Projects

- MerchantMiles
- Loyalty, fintech and banking platforms