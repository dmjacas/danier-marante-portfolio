# Security Architecture

## Experience

Applied to production private-banking systems: authentication and authorization enforced at the application boundary and service layer, with identity and access management (e.g. MerchantMiles).

## Authentication

Typical enterprise architecture:

```text
Client
  │
  ▼
Identity Provider
  │
  │ Access Token
  ▼
API Gateway
  │
  ▼
Backend Services
```

## Controls

- OAuth 2.0 / OpenID Connect
- JWT validation
- Role-based authorization
- Least-privilege IAM
- HTTPS/TLS
- Secure HTTP headers
- CORS configuration
- Input validation
- Rate limiting
- Secret management
- Audit logging

## Security principle

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

Both should be explicitly enforced at the appropriate architectural boundaries.

## Lessons Learned

- Security is an architectural concern, not a checklist (see [engineering principles](../docs/engineering-principles.md)).
- Protect sensitive data at rest, in transit and in logs.
- Least-privilege IAM reduces blast radius.

## Related

- [MerchantMiles (Security) →](../projects/merchant-miles/README.md)
- [Availability & Reliability](availability.md)
