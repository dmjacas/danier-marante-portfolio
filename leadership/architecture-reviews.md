# Architecture Reviews & Decision Making

## Purpose

Architecture reviews turn requirements into defensible technical decisions. The process makes the reasoning explicit so the decision can be challenged, recorded and revisited.

## Decision flow

```text
Business requirement
       ↓
Constraints
       ↓
Options
       ↓
Technical evaluation
       ↓
Trade-offs
       ↓
Decision
       ↓
Documentation
       ↓
Implementation
       ↓
Review (in production)
```

## How decisions are made

1. **Business requirement** — understand the problem being solved, not the technology to use.
2. **Constraints** — surface constraints early: business, technical, security, integration, deployment, operational, cost.
3. **Options** — list realistic alternatives, not only the familiar one. Every option gets a fair evaluation.
4. **Technical evaluation** — compare options against constraints: scalability, availability, security, performance, observability, maintainability, cost.
5. **Trade-offs** — name what is given up for each option (complexity, cost, latency, coupling).
6. **Decision** — choose and record it.
7. **Documentation** — record an ADR with Context → Problem → Options → Decision → Rationale → Trade-offs → Consequences.
8. **Implementation** — the team implements with the recorded decision as reference.
9. **Review** — verify in production through observability and metrics; revisit the decision when evidence contradicts it.

## Architecture review practice

- Reviews evaluate **architecture intent**, not just code: boundaries, contracts, failure handling, security, deployment.
- A decision is not final because it was made once; production evidence can reopen it.
- Reviews involve the people who will operate the system, not only those who build it.
- Open questions are recorded explicitly rather than resolved by assumption.

## Demonstrated in

- MerchantMiles: microservices decision (see [ADR-001 →](../docs/architecture-decisions/ADR-001-microservices.md)), PostgreSQL, AWS.
- AI architecture: embeddings retrieval decision (see [ADR-004 →](../docs/architecture-decisions/ADR-004-ai-embeddings.md)).

## Related

- [Technical Leadership →](technical-leadership.md)
- [Engineering Process →](engineering-process.md)
- [Architecture Decision Records →](../docs/architecture-decisions/)