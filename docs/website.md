# Website Launch Preparation

This repository is structured as the content source for a future Next.js portfolio website. Markdown is organized so it can be consumed and converted into web pages.

## Target routes

```text
/             → About, positioning, impact, featured work
/about        → profile + experience
/projects     → project case studies (projects/)
/architecture → architecture knowledge base + gallery (architecture/, diagrams/)
/ai           → AI engineering & MCP (ai/)
/leadership   → technical leadership (leadership/)
/experience   → professional experience (experience/)
/contact      → GitHub, LinkedIn, email
```

## Content readiness

- **projects/** — each project directory maps to `/projects/:slug`.
- **architecture/** — each Markdown maps to `/architecture/:doc`.
- **ai/** — maps to `/ai/:doc`.
- **leadership/** — maps to `/leadership/:doc`.
- **experience/** — maps to `/experience/:company`.
- **docs/architecture-decisions/** — maps to `/architecture/decisions/:adr`.
- **profile/skills.md** — `/skills` technology matrix.

## SEO focus

Conceptual metadata for the future site should reflect:

```text
Solution Architect · Software Architect · Senior Software Engineer
Technical Lead · Fintech · Banking · AWS · .NET · Node.js · React
Next.js · AI · MCP · Amazon Bedrock · Microservices · Distributed Systems
```

Use these naturally in page titles, descriptions and content — not as artificial keyword stuffing.

## Implementation notes

- Convert Markdown statically (e.g. Next.js + a Markdown pipeline).
- Preserve naming conventions so slugs map predictably.
- Diagrams: render Mermaid in `diagrams/README.md` and case studies.
- Keep routing conventions aligned with the repository structure above.

This repository remains the single source of truth; the website consumes it.