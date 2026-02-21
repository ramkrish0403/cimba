# Requirement Template Reference

This document defines the structure and format for each output file.

---

## README.md Structure

```markdown
# Feature: {Feature Name}

> {One-line description}

## Status
- [ ] Design Complete
- [ ] Implementation Started
- [ ] Implementation Complete
- [ ] Tested
- [ ] Deployed

## Quick Reference

| Aspect | Details |
|--------|---------|
| Task Folder | `{folder-name}` |
| Created | {YYYY-MM-DD HH:MM} |
| Target App | dashboard / command-center / both |
| Dependencies | {list of prerequisite features} |

## Documents

| Document | Description |
|----------|-------------|
| [requirements.md](./requirements.md) | Functional and non-functional requirements |
| [data-models.md](./data-models.md) | Entity definitions and relationships |
| [api-contracts.md](./api-contracts.md) | API endpoint specifications |
| [ia.md](./ia.md) | Information architecture, navigation |
| [ux.md](./ux.md) | User flows, interactions |
| [ui.md](./ui.md) | Components, layouts |
| [acceptance-criteria.md](./acceptance-criteria.md) | Testable success criteria |
| [scope.md](./scope.md) | Scope boundaries |

## Implementation Notes

{Any high-level notes for implementers}
```

---

## requirements.md Structure

```markdown
# Requirements: {Feature Name}

## Functional Requirements

### Core Functionality
| ID | Requirement | Priority | Depends On |
|----|-------------|----------|------------|
| REQ-001 | {Requirement text} | Must | - |
| REQ-002 | {Requirement text} | Should | REQ-001 |

### User Interactions
| ID | Requirement | Priority | Depends On |
|----|-------------|----------|------------|
| REQ-010 | {Requirement text} | Must | - |

### Data Management
| ID | Requirement | Priority | Depends On |
|----|-------------|----------|------------|
| REQ-020 | {Requirement text} | Must | - |

## Non-Functional Requirements

### Performance
| ID | Requirement | Metric |
|----|-------------|--------|
| NFR-001 | {Requirement text} | {Measurable metric} |

### Security
| ID | Requirement | Reference |
|----|-------------|-----------|
| NFR-010 | {Requirement text} | auth-foundations.md |

### Accessibility
| ID | Requirement | WCAG Level |
|----|-------------|------------|
| NFR-020 | {Requirement text} | AA |

## Constraints

| ID | Constraint | Reason |
|----|------------|--------|
| CON-001 | {Constraint text} | {Why this constraint exists} |
```

---

## data-models.md Structure

```markdown
# Data Models: {Feature Name}

## Entity Relationship Diagram

\`\`\`mermaid
erDiagram
    Entity1 ||--o{ Entity2 : contains
    Entity2 }|--|| Entity3 : belongs_to
\`\`\`

## Entities

### {EntityName}

**Description:** {What this entity represents}

**Zod Schema:**
\`\`\`typescript
import { z } from 'zod';

export const {EntityName}Schema = z.object({
  id: z.string().uuid(),
  // ... fields
  createdAt: z.date(),
  updatedAt: z.date(),
});

export type {EntityName} = z.infer<typeof {EntityName}Schema>;
\`\`\`

**Database Considerations:**
| Field | Type | Constraints | Index |
|-------|------|-------------|-------|
| id | UUID | PK | Yes |

**Relationships:**
| Related Entity | Type | Foreign Key |
|----------------|------|-------------|
| {Entity2} | One-to-Many | entity2_id |

## Enums

\`\`\`typescript
export const {EnumName} = z.enum(['value1', 'value2', 'value3']);
\`\`\`
```

---

## api-contracts.md Structure

```markdown
# API Contracts: {Feature Name}

## Endpoints Overview

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /api/{resource} | List all | Required |
| POST | /api/{resource} | Create new | Required |
| GET | /api/{resource}/:id | Get by ID | Required |
| PATCH | /api/{resource}/:id | Update | Required |
| DELETE | /api/{resource}/:id | Delete | Required |

## Endpoint Details

### GET /api/{resource}

**Description:** {What this endpoint does}

**Query Parameters:**
| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| page | number | No | 1 | Page number |
| limit | number | No | 20 | Items per page |

**Response (200):**
\`\`\`typescript
interface ListResponse {
  data: {Entity}[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}
\`\`\`

**Error Responses:**
| Status | Code | Description |
|--------|------|-------------|
| 401 | UNAUTHORIZED | Not authenticated |
| 403 | FORBIDDEN | Not authorized for this resource |

### POST /api/{resource}

**Request Body:**
\`\`\`typescript
interface Create{Entity}Request {
  // fields
}
\`\`\`

**Response (201):**
\`\`\`typescript
interface {Entity}Response {
  data: {Entity};
}
\`\`\`
```

---

## ia.md Structure

```markdown
# Information Architecture: {Feature Name}

## Navigation Structure

\`\`\`
{App Root}
├── {Section}
│   ├── {Subsection}
│   └── {Subsection}
└── {Section}
\`\`\`

## Data Hierarchy

| Level | Entity | Parent | Children |
|-------|--------|--------|----------|
| 1 | {Entity} | None | {Child entities} |
| 2 | {Entity} | {Parent} | {Child entities} |

## Content Organization

| Content Type | Location | Access Pattern |
|--------------|----------|----------------|
| {Content} | {Where it lives} | {How users find it} |

## URL Structure

| Route | Page | Parameters |
|-------|------|------------|
| `/feature` | List view | - |
| `/feature/:id` | Detail view | id: string |
| `/feature/:id/edit` | Edit view | id: string |
```

---

## ux.md Structure

```markdown
# User Experience: {Feature Name}

## User Flows

### Flow 1: {Flow Name}

\`\`\`mermaid
flowchart TD
    A[Start] --> B[Action]
    B --> C{Decision}
    C -->|Yes| D[Result 1]
    C -->|No| E[Result 2]
\`\`\`

## Interaction Patterns

| Action | Trigger | Feedback | Result |
|--------|---------|----------|--------|
| {Action} | {Click/Hover/etc} | {Visual feedback} | {Outcome} |

## State Transitions

| Current State | Event | Next State | Side Effects |
|---------------|-------|------------|--------------|
| {State} | {Event} | {State} | {API call, etc} |

## Error Handling

| Error Type | User Message | Recovery Action |
|------------|--------------|-----------------|
| {Error} | {Friendly message} | {What user can do} |

## Loading States

| Context | Loading Indicator | Skeleton |
|---------|-------------------|----------|
| {Page/Component} | {Spinner/Progress} | {Yes/No} |

## Empty States

| Context | Message | Action |
|---------|---------|--------|
| {When empty} | {Helpful message} | {CTA button} |
```

---

## ui.md Structure

```markdown
# User Interface: {Feature Name}

## Component Hierarchy

\`\`\`
{FeaturePage}
├── {FeatureHeader}
│   ├── Title
│   └── ActionButtons
├── {FeatureList} or {FeatureGrid}
│   └── {FeatureCard}
└── {FeatureEmptyState}
\`\`\`

## shadcn/ui Components

| Component | Usage | Variant | Notes |
|-----------|-------|---------|-------|
| Card | Container for items | default | Use CardHeader, CardContent |
| Button | Primary actions | default | variant="default" for primary |
| Dialog | Confirmation, forms | default | Use for create/edit |

## Layout Specifications

| Section | Layout | Spacing | Max Width |
|---------|--------|---------|-----------|
| {Section} | {Grid/Flex/Stack} | {Tailwind class} | {max-w-*} |

## Responsive Behavior

| Breakpoint | Behavior |
|------------|----------|
| Mobile (<640px) | Stack vertically |
| Tablet (640-1024px) | 2-column grid |
| Desktop (>1024px) | 3-column grid |

## State Management

| State | Type | Location | Reason |
|-------|------|----------|--------|
| {stateName} | Server | TanStack Query | Synced with backend |
| {uiState} | Client | Zustand | UI-only state |

## Accessibility

| Requirement | Implementation |
|-------------|----------------|
| Keyboard navigation | Tab order, Enter/Space activation |
| Screen reader | aria-labels, semantic HTML |
| Focus indicators | Ring on focus-visible |
```

---

## acceptance-criteria.md Structure

```markdown
# Acceptance Criteria: {Feature Name}

## Core Functionality

### AC-001: {Criteria Title}
**Requirement:** REQ-001

**Scenario: {Scenario name}**
- **Given** {initial context}
- **When** {action is taken}
- **Then** {expected outcome}

**Scenario: {Edge case}**
- **Given** {edge case context}
- **When** {action is taken}
- **Then** {expected outcome}

## Error Handling

### AC-010: {Error Scenario}
**Requirement:** REQ-005

- **Given** {context that causes error}
- **When** {action is taken}
- **Then** {error is handled gracefully}
- **And** {user sees helpful message}

## Integration Tests

| AC ID | Test File | Test Name |
|-------|-----------|-----------|
| AC-001 | {feature}.test.tsx | should {behavior} |
```

---

## scope.md Structure

```markdown
# Scope: {Feature Name}

## In Scope

### Must Have (P0)
- [ ] {Item 1}
- [ ] {Item 2}

### Should Have (P1)
- [ ] {Item 3}

### Nice to Have (P2)
- [ ] {Item 4}

## Out of Scope

| Item | Reason | Future Consideration |
|------|--------|---------------------|
| {Item} | {Why excluded} | v2.0 / Never |

## Dependencies

### Requires Before Implementation
| Dependency | Status | Notes |
|------------|--------|-------|
| {Feature/Component} | Done/Pending | {Notes} |

### Will Enable After Implementation
| Feature | How This Helps |
|---------|----------------|
| {Future feature} | {Connection} |

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {Risk} | High/Med/Low | High/Med/Low | {Mitigation} |
```
