# Feature Specification Template

> Copy this template to create a new feature specification folder.
> Replace all {placeholders} with actual values.

---

## Folder Structure

```
tasks/{YYYY_MMDD_HHMMSS}_{feature-name}/
├── README.md
├── requirements.md
├── data-models.md
├── api-contracts.md
├── ia.md
├── ux.md
├── ui.md
├── acceptance-criteria.md
└── scope.md
```

---

## README.md

```markdown
# Feature: {Feature Name}

> {One-line description of what this feature enables}

## Status

- [x] Design Complete
- [ ] Implementation Started
- [ ] Implementation Complete
- [ ] Tested
- [ ] Deployed

## Quick Reference

| Aspect | Details |
|--------|---------|
| Task Folder | `{YYYY_MMDD_HHMMSS}_{feature-name}` |
| Created | {YYYY-MM-DD HH:MM} |
| Target App | dashboard |
| Dependencies | {comma-separated list or "None"} |

## Summary

{2-3 sentence summary of the feature, its purpose, and key functionality}

## Key Entities

- **{Entity1}**: {Brief description}
- **{Entity2}**: {Brief description}

## Key Endpoints

| Endpoint | Purpose |
|----------|---------|
| `GET /api/{resource}` | {Purpose} |
| `POST /api/{resource}` | {Purpose} |

## Documents

| Document | Description |
|----------|-------------|
| [requirements.md](./requirements.md) | {X} functional, {Y} non-functional requirements |
| [data-models.md](./data-models.md) | {N} entities with Zod schemas |
| [api-contracts.md](./api-contracts.md) | {M} API endpoints |
| [ia.md](./ia.md) | Information architecture, navigation |
| [ux.md](./ux.md) | User flows, interactions |
| [ui.md](./ui.md) | Components, layouts |
| [acceptance-criteria.md](./acceptance-criteria.md) | {P} testable criteria |
| [scope.md](./scope.md) | Scope boundaries and risks |

## Implementation Notes

- Follow feature module pattern from `react-stack-guide.md`
- Use Orval for API hook generation
- Reference existing patterns in `features/` folder
```

---

## Quick Checklist

Before finalizing specification:

- [ ] All requirements are numbered (REQ-XXX)
- [ ] Each requirement is atomic and testable
- [ ] Data models have Zod schemas
- [ ] API contracts have TypeScript types
- [ ] Acceptance criteria use Given/When/Then format
- [ ] Scope clearly defines in/out boundaries
- [ ] Dependencies are identified
- [ ] Risks are documented with mitigations

---

## Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Task folder | `YYYY_MMDD_HHMMSS_feature-name` | `2026_0101_143022_workspaces` |
| Requirement ID | `REQ-XXX` | `REQ-001` |
| Non-functional | `NFR-XXX` | `NFR-001` |
| Constraint | `CON-XXX` | `CON-001` |
| Acceptance Criteria | `AC-XXX` | `AC-001` |

---

## Priority Definitions

| Priority | Label | Meaning |
|----------|-------|---------|
| P0 | Must Have | Required for feature to function |
| P1 | Should Have | Important but not blocking |
| P2 | Nice to Have | Can be deferred |
| P3 | Future | Out of scope for initial implementation |
