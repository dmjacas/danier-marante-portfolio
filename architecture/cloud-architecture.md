# Cloud Architecture

## Experience

Applied to production platforms on AWS: managed storage, CDN, identity and access management, serverless components where appropriate, and Infrastructure as Code for reproducibility (e.g. MerchantMiles).

## Reference AWS Architecture

```text
                         Internet
                            │
                            ▼
                     ┌─────────────┐
                     │ CloudFront  │
                     └──────┬──────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
          S3 / Frontend              API Gateway
                                          │
                                          ▼
                                   Application Layer
                                          │
                           ┌──────────────┼──────────────┐
                           ▼              ▼              ▼
                        Lambda       Containers      Services
                           │              │              │
                           └──────────────┼──────────────┘
                                          ▼
                                     PostgreSQL
```

## Principles

- Managed services where they reduce operational burden
- Least-privilege IAM
- Secrets stored outside source code
- Infrastructure as Code
- Automated deployments
- Centralized monitoring and logging
- Encryption in transit and at rest
- Backups and disaster recovery
- Cost visibility

## Infrastructure as Code

Terraform can be used to define:

- Networking
- IAM
- Compute
- Storage
- Databases
- CDN
- Serverless infrastructure
- Monitoring

## Lessons Learned

- Managed services reduce operational burden but require IAM, cost and lifecycle discipline.
- Infrastructure as Code makes environments reproducible and reviewable.
- Availability is architected, not only measured (see [Availability & Reliability](availability.md)).

## Related

- [MerchantMiles (Cloud) →](../projects/merchant-miles/README.md)
- [ADR-003 — AWS →](../docs/architecture-decisions/ADR-003-aws.md)
