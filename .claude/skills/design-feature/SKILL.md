---
name: design-feature
description: "Creates detailed feature requirements and scope documents. Leverages LLM's ability to read codebase, documentation, and tech stack to produce lower-level specifications than traditional human requirements. Outputs to tasks folder with timestamped directories."
license: MIT
metadata:
  version: 2.0.0
  model: claude-opus-4-5-20251101
  domains: [requirements, design, planning, documentation]
  type: generator
  inputs: [feature-name, feature-goal]
  outputs: [requirements.md, data-models.md, api-contracts.md, ia.md, ux.md, ui.md, acceptance-criteria.md, scope.md]
---

# Design Feature

Creates comprehensive feature specifications by analyzing the codebase, documentation, and tech stack.

---

## Quick Start

```
/design-feature workspaces
/design-feature user-authentication
design feature for workflow execution engine
```

---

## Triggers

- `/design-feature <feature-name>` - Primary trigger
- `design feature for <goal>` - Natural language
- `create requirements for <feature>` - Alternative phrasing

---

## What This Skill Does

Unlike human-written requirements (which stay abstract due to knowledge gaps), this skill produces **lower-level specifications** because it can:

| LLM Advantage | How It Helps |
|---------------|--------------|
| **Reads codebase** | References actual file paths, existing patterns |
| **Reads all docs** | Understands Org → Team → Workspace hierarchy |
| **Knows tech stack** | TanStack Router, Zustand, Orval, Zod, shadcn/ui |
| **Specifies precisely** | Exact Zod schemas, API endpoint shapes, component props |
| **Ensures consistency** | References ui-design-guide.md tokens, react-stack-guide.md patterns |

---

## Output Structure

Creates a timestamped folder in `/workspaces/reflow/tasks/`:

```
tasks/YYYY_MMDD_HHMMSS_<feature-name>/
├── README.md                   # Overview, status, quick reference
├── requirements.md             # Functional and non-functional requirements
├── data-models.md              # Entity definitions, relationships, Zod schemas
├── api-contracts.md            # Endpoints, request/response types
├── ia.md                       # Information architecture, navigation, data hierarchy
├── ux.md                       # User flows, interactions, state transitions
├── ui.md                       # Components, layouts, design tokens
├── acceptance-criteria.md      # Testable success criteria (Given/When/Then)
└── scope.md                    # In-scope, out-of-scope, future considerations
```

---

## Process

```
1. LOAD CONTEXT
   ├── Read infrastructure/documentation/*.md
   ├── Scan existing codebase structure
   └── Identify related existing features

2. ANALYZE FEATURE
   ├── Break down into sub-features
   ├── Identify data entities
   ├── Map to existing patterns
   └── Note integration points

3. GENERATE SPECIFICATIONS
   ├── Create task folder with timestamp
   ├── Write each document
   └── Cross-reference between documents

4. VALIDATE
   ├── Check completeness
   ├── Verify consistency with existing patterns
   └── Ensure acceptance criteria are testable
```

---

## Documentation Context

The skill reads these documents to inform specifications:

| Document | Used For |
|----------|----------|
| `project-goals.md` | Org/Team/Workspace hierarchy, ABAC model, product vision |
| `react-stack-guide.md` | Feature module pattern, tech stack, code conventions |
| `ui-design-guide.md` | Design tokens, colors, typography, spacing |
| `ui-design-principles.md` | UX patterns, interaction guidelines |
| `auth-foundations.md` | Authentication patterns, session management |
| `access-control-architecture.md` | ABAC/Cerbos patterns, policy structure |
| `monorepo-setup.md` | Nx workspace structure, package organization |

---

## Output Quality Standards

### Requirements (requirements.md)
- Numbered for traceability (REQ-001, REQ-002)
- Categorized: Functional, Non-Functional, Constraints
- Each requirement is atomic and testable
- Dependencies between requirements noted

### Data Models (data-models.md)
- Entity diagrams (Mermaid)
- Zod schema definitions
- Relationship mappings
- Database table considerations

### API Contracts (api-contracts.md)
- REST endpoint definitions
- Request/response TypeScript types
- Error response shapes
- OpenAPI-compatible format

### Information Architecture (ia.md)
- Navigation structure
- Data hierarchy and relationships
- Content organization
- URL structure and routing

### User Experience (ux.md)
- User flows (Mermaid diagrams)
- Interaction patterns
- State transitions
- Error handling flows
- Loading and empty states

### User Interface (ui.md)
- Component hierarchy
- shadcn/ui component mapping
- Layout specifications
- Responsive behavior
- Accessibility requirements

### Acceptance Criteria (acceptance-criteria.md)
- Given/When/Then format
- Covers happy path and edge cases
- Maps to requirements
- Testable with integration tests

### Scope (scope.md)
- Explicit in-scope items
- Explicit out-of-scope items
- Future enhancement possibilities
- Dependencies on other features

---

## Example Usage

```
User: /design-feature workspaces

Claude: I'll design the Workspaces feature. Let me first read the project documentation...

[Reads documentation]

Creating task folder: tasks/2026_0101_143022_workspaces/

[Generates all specification documents]

Feature specification complete. Key highlights:
- 12 functional requirements identified
- 4 entities: Workspace, WorkspaceMember, WorkspaceSettings, WorkspaceInvite
- 8 API endpoints for CRUD + member management
- Kanban and list views for workspace switching
- 15 acceptance criteria covering core flows

Ready for implementation with /implement-feature 2026_0101_143022_workspaces
```

---

## Feedback Log

> This section captures generalizable lessons learned from using this skill.
> When feedback is given that could improve future runs, add it here.

| Date | Feedback | Incorporated Change |
|------|----------|---------------------|
| - | - | - |

---

## Related Skills

| Skill | Relationship |
|-------|--------------|
| `/implement-feature` | Implements features based on these specifications |
| `SkillForge` | Created this skill |

---

## Extension Points

1. **Custom templates**: Add domain-specific templates to `assets/templates/`
2. **Additional doc types**: Extend output structure for specific needs
3. **Integration hooks**: Add pre/post processing scripts
