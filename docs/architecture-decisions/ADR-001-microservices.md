# ADR-001 — Microservices

## Status

Accepted

## Context

Some business capabilities require independent ownership, deployment and scaling.

## Decision

Use service-oriented boundaries around meaningful business capabilities rather than creating services purely around technical layers.

## Consequences

### Positive

- Independent deployment
- Independent scaling
- Clear ownership
- Reduced coupling

### Negative

- Distributed-system complexity
- Network failures
- More operational tooling
- Higher observability requirements
