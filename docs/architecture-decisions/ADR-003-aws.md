# ADR-003 — AWS

## Status

Accepted

## Context

Solutions require scalable managed infrastructure, security controls and cloud-native services.

## Problem

Which cloud platform to use for production workloads, considering reliability, scalability, operational effort and cost.

## Options Considered

### Option 1 — Azure

- Pros: strong enterprise identity integration.
- Cons: different managed-service catalog; not the primary footprint for the products in this portfolio.

### Option 2 — On-premise/self-managed

- Pros: full control.
- Cons: high operational effort, slower scaling, no managed services.

### Option 3 — AWS

- Pros: broad managed-service catalog, mature serverless options, strong ecosystem and IaC support.
- Cons: requires disciplined IAM, cost controls and operational knowledge.

## Decision

Use AWS where its managed services provide a good balance between reliability, scalability, operational effort and cost.

## Rationale

AWS provided the managed components (object storage, CDN, IAM, serverless, compute) needed for cloud-native platforms, with Infrastructure as Code reproducibility.

## Trade-offs

### Advantages

- Managed services reduce operational burden
- Scalable compute, storage and serverless options
- Strong ecosystem and tooling

### Disadvantages

- IAM, cost controls and observability must be actively managed
- Cloud-specific operational knowledge required

## Consequences

- The team must manage IAM, cost controls, observability, infrastructure lifecycle and cloud-specific operational knowledge.
- Infrastructure as Code (e.g. Terraform) is used for reproducibility (see engineering principles).

## Related Projects

- MerchantMiles
- Chaide
- GreenCloud

## Related ADRs

- [ADR-001 — Microservices](./ADR-001-microservices.md)