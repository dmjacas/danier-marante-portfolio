# Metrics Inventory

Classification of the metrics this portfolio could demonstrate. This inventory is used to decide which metrics are public, validated or confidential.

**Rules**

- Only real, shareable, validated metrics are published.
- A metric that exists but cannot be shared is marked `[Confidential]`.
- A metric that exists but is not yet confirmed is marked `[Metric to validate]`.
- A metric that does not exist is not claimed.

## Business

| Metric | Source project | Status |
|---|---|---|
| Countries served | MerchantMiles (Ecuador + Central America) | Validated (public) |
| Banks / banking clients | MerchantMiles (Clubmiles, Promerica) | Validated (public) |
| Organizations | GreenCloud (Intel CR, Coca-Cola Bolivia, CAF, BCIE) | Validated (client names) |
| Merchants | MerchantMiles | `[Metric to validate]` / `[Confidential]` |
| Campaigns | MerchantMiles | `[Metric to validate]` / `[Confidential]` |
| Users / cardholders | MerchantMiles | `[Metric to validate]` / `[Confidential]` |
| Branches | MerchantMiles | `[Metric to validate]` / `[Confidential]` |
| Transactions / volume | MerchantMiles; Chaide | `[Metric to validate]` / `[Confidential]` |
| Customers | Neutralfy; Chaide | `[Metric to validate]` / `[Confidential]` |
| Insurance sales | EasyBrok | `[Metric to validate]` / `[Confidential]` |

## Technical

| Metric | Source project | Status |
|---|---|---|
| Requests | General | `[Metric to validate]` / `[Confidential]` |
| Latency | General | `[Metric to validate]` / `[Confidential]` |
| Throughput | General | `[Metric to validate]` / `[Confidential]` |
| Availability | General | Not disclosed — no SLA/uptime claim is made without validated public evidence |
| Error rate | General | `[Metric to validate]` / `[Confidential]` |
| Deployment frequency | General | `[Metric to validate]` / `[Confidential]` |
| Build time | General | `[Metric to validate]` / `[Confidential]` |
| Processing time (data) | MerchantMiles (data processing) | `[Metric to validate]` / `[Confidential]` |

## Operational

| Metric | Source project | Status |
|---|---|---|
| Incidents | General | `[Metric to validate]` / `[Confidential]` |
| Recovery time | General | `[Metric to validate]` / `[Confidential]` |
| Infrastructure cost | General | `[Confidential]` |
| Automation time savings | AI automation | `[Metric to validate]` / `[Confidential]` |

## AI

| Metric | Source project | Status |
|---|---|---|
| Documents generated | `ppm-doc` MCP | `[Metric to validate]` — no public metrics |
| Tokens / cost | AI workloads | `[Confidential]` |
| Processing time | AI automation | `[Metric to validate]` / `[Confidential]` |
| Manual steps removed | AI automation | `[Metric to validate]` / `[Confidential]` |
| Automation % | AI automation | `[Metric to validate]` / `[Confidential]` |

## What is published today

- Countries, banks and client names: published (MerchantMiles, GreenCloud).
- Everything else: placeholder or omitted until validated/confirmed.

## Next steps

1. Review each `[Metric to validate]` with the source and confirm public/confidential.
2. Replace confirmed public metrics in the relevant project documents.
3. Keep `[Confidential]` markers instead of values for anything that cannot be shared publicly.