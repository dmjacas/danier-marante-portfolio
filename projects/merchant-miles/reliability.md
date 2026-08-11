# MerchantMiles Reliability

> Classification follows V4 rules: **Implemented** (validated with project owner), **Recommended** (hardening), **Requires validation** (`[Metric to validate]`).

## Reliability Goals

- Keep the loyalty platform operational during campaign peaks (business-critical demand pattern).
- Protect the private-banking data plane: authentication, benefits and campaign flows.
- Diagnose distributed failures quickly through observability.
- Recover from failures without corrupting state (idempotency on high-value flows).

## Availability

Availability is architected, not measured afterwards. The platform is designed around failure domains and dependency failures. No availability percentage is claimed without validated public evidence.

## Failure Domains

- Application (code, configuration, resource exhaustion)
- Database (per service — connection issues, slow queries, disk, replication lag)
- External APIs (financial/commerce integrations)
- Network (DNS, connectivity, timeouts)
- Infrastructure (compute, storage, availability zone)
- Deployment (bad release, migration failure)
- Authentication (identity provider outage)

## Failure Scenarios

### Database unavailable

**Implemented:** connection timeouts; managed database handling; monitoring of health.

**Recommended:** managed failover validation; replication-lag alerting `[Metric to validate]`.

### External provider unavailable

**Implemented:** integrations isolated behind contracts; timeouts; retries with backoff where safe; circuit breakers; idempotency.

**Recommended:** per-integration tuning of retry/backoff thresholds `[Metric to validate]`.

### Authentication unavailable

**Implemented:** centralized authentication at the application boundary; only authenticated flows are allowed.

**Recommended:** cached/validated token resilience `[Metric to validate]`.

### Service unavailable

**Implemented:** services scale independently; health checks detect unavailability; consumers use timeouts and retries.

**Recommended:** readiness-based traffic draining `[Metric to validate]`.

### Network failure

**Implemented:** distributed-systems discipline — timeouts, retries with backoff, graceful degradation of non-essential features.

### Deployment failure

**Implemented:** CI/CD with reviewable changes and a rollback path; health checks gating traffic.

## Availability Matrix

| Failure | Impact | Detection | Mitigation | Recovery |
|---|---|---|---|---|
| Database unavailable | High | Monitoring/health | Timeouts, managed handling | `[Metric to validate]` |
| External API unavailable | Medium/High | Timeouts, circuit breaker | Retries w/ backoff, circuit breaker | `[Metric to validate]` |
| Authentication unavailable | High | Boundary enforcement | Centralized auth | `[Metric to validate]` |
| Service unavailable | Medium | Health checks | Service isolation | `[Metric to validate]` |
| Deployment failure | High | CI/CD, health checks | Rollback path | `[Metric to validate]` |

## Dependency Failures

Every external dependency is classified by blast radius and handled with the appropriate combination of timeouts, retries, circuit breakers and idempotency.

## Timeout Strategy

**Implemented:** every external interaction is bounded by a timeout.

## Retry Strategy

**Implemented:** retries only where safe (idempotent operations), with backoff.

## Idempotency

**Implemented:** high-value flows are idempotent so repeated operations do not corrupt state.

## Circuit Breakers

**Implemented:** circuit breakers prevent hammering a failing dependency.

## Health Checks

**Implemented:** health/readiness checks used for routing and orchestration.

## Observability

- Structured logs
- Metrics (latency, errors, saturation)
- Trace correlation for distributed diagnosis
- Alerts with actionable thresholds

## Deployment Reliability

- CI/CD with reviewable changes
- Rollback path for failed releases
- Health checks gating traffic
- Infrastructure as Code for reproducible environments

## Recovery

- Rollback path for failed releases.
- Healthy-state verification after incidents.
- Incident follow-up fed back into architecture decisions.

## Disaster Recovery

`[Metric to validate]` — disaster-recovery specifics are not publicly documented.

## Metrics

> Production availability metrics are not publicly disclosed. No availability percentage, SLA or uptime claim is made without validated public evidence.

## Related

- [Availability & Reliability architecture →](../../architecture/availability.md)
- [MerchantMiles case study →](README.md)
- [Data Architecture →](data-architecture.md)
- [ADR-002 — PostgreSQL →](../../docs/architecture-decisions/ADR-002-postgresql.md)
- [ADR-003 — AWS →](../../docs/architecture-decisions/ADR-003-aws.md)