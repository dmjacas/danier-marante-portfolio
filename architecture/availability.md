# Availability & Reliability

How availability is treated as a first-class architectural concern during design, delivery and operation.

## Availability

Availability is designed, not measured afterwards. For every important solution the question is:

> What happens when dependencies fail?

Availability is architected through failure domains, failure handling, observability and reliable deployment — not by quoting SaaS percentages.

## Failure Domains

What can fail:

- Application (code, configuration, resource exhaustion)
- Database (connection issues, slow queries, disk, replication lag)
- External APIs (third-party providers, financial/commerce integrations)
- Network (DNS, connectivity, timeouts)
- Infrastructure (compute, storage, availability zone)
- Deployment (bad release, migration failure)
- Authentication (identity provider outage)
- Third-party services (payments, messaging)

## Failure Handling

- **Timeouts** — every external interaction bounded by a timeout.
- **Retries** — only where safe (idempotent operations), with backoff.
- **Circuit breakers** — stop hammering a failing dependency.
- **Idempotency** — repeated operations must not corrupt state.
- **Graceful degradation** — core paths degrade, not the whole system.
- **Health checks** — alive/ready probes for routing and orchestration.
- **Backoff and jitter** — avoid thundering herds on recovery.

## Observability

Diagnosing failures quickly is part of availability:

- Structured logs
- Metrics (latency, errors, saturation)
- Distributed traces
- Alerts with actionable thresholds

## Deployment Reliability

- CI/CD with reviewable changes
- Rollback path for failed releases
- Health checks gating traffic
- Infrastructure as Code for reproducible environments
- Database migrations handled as release steps

## Disaster Recovery / Business Continuity

Only documented where actually implemented in a specific system. See project-specific reliability documents (e.g. [MerchantMiles reliability](../projects/merchant-miles/reliability.md)).

## Metrics

**Validated production metrics only.**

No availability percentages, SLAs or uptime figures are claimed in this portfolio unless they are real, publicly shareable and validated. When unavailable:

> Production availability metrics are not publicly disclosed.

## Related

- [Scalability](scalability.md)
- [Distributed Systems](distributed-systems.md)
- [Security Architecture](security.md)
- [Engineering principles — Observability](../docs/engineering-principles.md)