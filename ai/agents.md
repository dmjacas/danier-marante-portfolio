# AI Agents

## Goal

Use AI agents where they create measurable value: capable of planning steps and calling tools, while deterministic business rules remain in code.

## Agent architecture

```text
User Request
    ↓
Agent / Orchestrator
    ↓
├──► Tool: MCP / API / Search
├──► Tool: Retrieval / Vector Store
└──► Tool: Business Service (deterministic)
    ↓
Validated Response / Action
```

## Practices

- Agents orchestrate; business rules stay outside prompts.
- Tool results are validated before they are used for decisions.
- High-impact actions require human approval.
- LLMs are treated as probabilistic components: outputs are measured and validated.
- Failures are made explicit and observable.

## Guardrails

- Input/output validation.
- Sensitive data protection.
- Evaluation and monitoring of quality and latency.
- Deterministic fallbacks for critical operations.

## Relationship to MCP

Agents consume capabilities exposed through tools; MCP provides a standard protocol for those tools. See the [MCP case study](mcp.md).