# Team Obsidian — System Architecture Blueprint

## 1. High-Level Overview
Team Obsidian ingests organizational knowledge across 8 distinct SaaS platforms into a unified architectural knowledge graph:
- **Code & Version Control**: GitHub & GitLab
- **Communication & Incident Rooms**: Slack
- **Specifications & Runbooks**: Notion & Confluence
- **Issue Tracking & Roadmaps**: Jira Cloud & Linear
- **Runtime Telemetry & Error Streams**: Sentry

## 2. Ingestion & Graph Protocol
```
[SaaS Connectors] -> [Nango Universal Gateway] -> [AST Tree-sitter Engine] -> [Unified Graph DB]
                                                          |
                                                 [Sentry Telemetry]
```

## 3. Resilience & Multi-Tenant Boundaries
- All provider credentials are encrypted at rest using AES-256-GCM.
- Per-tenant database row-level security isolates customer graphs.
- Webhook signature verification guarantees cryptographic integrity.
