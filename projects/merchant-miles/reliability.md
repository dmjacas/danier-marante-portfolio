# MerchantMiles Reliability

> Design intent is documented separately from implemented mechanisms. A pattern listed under *Design* is an architectural decision; a pattern listed under *Implemented* is documented as in place.

## Reliability Goals

- Keep the loyalty platform operational during campaign peaks (business-critical demand pattern).
- Protect the private-banking data plane: authentication, benefits and campaign flows.
- Diagnose distributed failures quickly through observability.
- Recover from failures without corrupting state (idempotency on high-value flows).

## Failure Scenarios

### Database unavailable

Design: connection timeouts, managed database failover where available, monitoring of replication/health.

Implemented: `[Metric to validate]` — recovery details not publicly documented.

### External provider unavailable

Design: external financial/commerce integrations isolated behind contracts, with timeouts, retries where safe, circuit breakers and idempotency.

Implemented: `[Metric to validate]`.

### Authentication unavailable

Design: centralized authentication at the application boundary; platform degrades only for authenticated flows.

Implemented: `[Metric to validate]`.

### Service unavailable

Design: services scale independently; health checks detect unavailability; consumers use timeouts and retries.

Implemented: `[Metric to validate]`.

### Network failure

Design: distributed-systems discipline — timeouts, retries with backoff, graceful degradation of non-essential features.

Implemented: `[Metric to validate]`.

## Availability Matrix

| Failure | Impact | Mitigation | Recovery |
|---|---|---|---|
| Database unavailable | High | Timeouts, managed failover (design) | `[Metric to validate]` |
| External API unavailable | Medium/High | Timeout / retry / circuit breaker (design) | `[Metric to validate]` |
| Authentication unavailable | High | Centralized auth boundary | `[Metric to validate]` |
| Service unavailable | Medium | Health checks, service isolation | `[Metric to validate]` |
| Deployment failure | High | CI/CD, reviewable changes, rollback path | `[Metric to validate]` |

## Mitigation

- Timeouts and retries only where safe.
- Idempotency for high-value flows.
- Graceful degradation rather than cascading failure.
- Health checks and readiness gating.
- Backoff/jitter to avoid thundering herds.

## Observability

- Structured logs
- Metrics (latency, errors, saturation)
- Trace correlation for distributed diagnosis
- Alerts with actionable thresholds

## Recovery

- Rollback path for failed releases.
- Healthy-state verification after incidents.
- Incident follow-up fed back into architecture decisions.

## Availability Metrics

> Production availability metrics are not publicly disclosed. No availability percentage, SLA or uptime claim is made.

## Related

- [Availability & Reliability architecture →](../../architecture/availability.md)
- [MerchantMiles case study →](README.md)
- [ADR-002 — PostgreSQL →](../../docs/architecture-decisions/ADR-002-postgresql.md)
- [ADR-003 — AWS →](../../docs/architecture-decisions/ADR-003-aws.md)