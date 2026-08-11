# Project Template

This template standardizes project documentation. Use `[TBD]` for any section where information is not yet confirmed. Do not invent metrics, clients or responsibilities.

**Required:** Executive Summary, Business Problem, Solution, My Role, Architecture, Technology, Results (or `[TBD]`).

## Template

```markdown
# Project Name

## Executive Summary

[What it is, who uses it, what problem it solves — no jargon.]

## Business Problem

[The problem the project solves for its users/organization.]

## Solution

[What was built to solve the problem.]

## My Role

- **Leadership** — [...]
- **Architecture** — [...]
- **Engineering** — [...]

## Architecture

[Diagram (Mermaid or ASCII) + explanation.]

## Technology

[Stack evidence: frontend, backend, data, cloud, DevOps.]

## Integrations

[Known external systems/APIs.]

## Key Decisions

[Decisions with context, options, rationale, trade-offs.]

## Challenges

[Problem / Solution / Result — result `[TBD]` if not validated.]

## Trade-offs

[What was chosen vs what was given up, and why.]

## Security

[Threats and controls relevant to this project.]

## Scalability

[How growth is absorbed.]

## Reliability

[Timeouts, retries, idempotency, async handling where applicable.]

## Results

[Validated outcomes only. Mark unknown metrics `[Metric to validate]` / `[TBD]`.]

## Lessons Learned

[Architectural and engineering lessons.]
```

## Usage

- Small projects (few confirmed details) may use the abbreviated form: Executive Summary, Business Problem, My Role, Architecture, Technology, Results.
- Tier 1 featured projects should follow the full template.
- Never `[TBD]` real data into a claim; keep placeholders explicit.