# Event-Driven Architecture

## Context

Some workloads are naturally asynchronous: data processing, notifications, reporting pipelines, integrations that should not block the main request path.

## Problem

Synchronous composition couples producers and consumers, reduces resilience, and does not scale when bursts of work arrive.

## Options

1. Synchronous request/response for everything.
2. Message queue between producer and single consumer.
3. Event bus / publish-subscribe with multiple consumers.

## Decision

Use event-driven messaging where work is asynchronous or when multiple consumers must react to the same occurrence. Retain synchronous request/response for low-latency, transaction-critical paths.

## Trade-offs

### Advantages

- Decoupling between producers and consumers.
- Burst tolerance via queuing/buffering.
- Independent scaling of consumers.

### Disadvantages

- Eventual consistency requires reconciliation.
- Causality and debugging are harder across consumers.
- Requires idempotency and ordering considerations.
- More operational components (brokers, DLQs, dead-letter handling).

## Consequences

- Events need explicit schemas and versioning.
- Consumers must be idempotent.
- Asynchronous processing must be made explicit in the architecture, per MerchantMiles lessons.
- Observability must correlate producer/consumer across tracing.

## Related

- [Distributed Systems](distributed-systems.md)
- [MerchantMiles — asynchronous processing](../projects/merchant-miles/README.md)