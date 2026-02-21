---
name: implement-feature
description: "Implements features based on specifications created by design-feature skill. Creates an implementation folder with plan, PR breakdown, tracker, and task files. Executes tasks with human approval gates between each PR-sized unit. Human manages all git operations."
license: MIT
metadata:
  version: 3.0.0
  model: claude-opus-4-5-20251101
  domains: [implementation, coding, feature-development]
  type: orchestrator
  inputs: [task-folder]
  outputs: [feature-module, api-integration, unit-tests, integration-tests, e2e-tests, docs-updates]
---

# Implement Feature

Implements features based on specifications from the `/design-feature` skill with **persistent session tracking**.

---

## Quick Start

```
/implement-feature 2026_0101_143022_workspaces
/implement-feature 2026_0101_150045_user-auth
```

**Resume Previous Session:**
```
/implement-feature 2026_0101_143022_workspaces --resume
```

**Note:** Task folder is always required. Use the folder name from `/workspaces/reflow/tasks/`.

---

## Triggers

- `/implement-feature <task-folder>` - Primary trigger (required)
- `/implement-feature <task-folder> --resume` - Resume from tracker
- `implement feature <task-folder>` - Natural language
- `build feature from <task-folder>` - Alternative phrasing
- `continue implementing <task-folder>` - Resume previous session

---

## Implementation Folder Structure

When implementing a feature, create this structure inside the tasks folder:

```
tasks/{task-folder}/
├── README.md                 # Feature overview (from design-feature)
├── requirements.md           # Requirements (from design-feature)
├── data-models.md            # Data models (from design-feature)
├── api-contracts.md          # API contracts (from design-feature)
├── ia.md                     # Information architecture (from design-feature)
├── ux.md                     # User experience (from design-feature)
├── ui.md                     # User interface (from design-feature)
├── acceptance-criteria.md    # Acceptance criteria (from design-feature)
│
└── implementation/           # *** CREATED BY THIS SKILL ***
    ├── plan.md               # High-level plan with stages/tasks
    ├── pr-breakdown.md       # PR-sized units with scope and tests
    ├── tracker.md            # Status tracking for session continuity
    ├── shared-context.md     # Common patterns, naming, interfaces
    │
    └── tasks/                # Individual task detail files
        ├── pr-1/
        │   ├── task-1.1-entity-schema.md
        │   ├── task-1.2-crud-service.md
        │   └── ...
        ├── pr-2/
        │   └── ...
        ├── pr-N-e2e/         # E2E tests PR
        │   └── task-e2e-happy-paths.md
        └── pr-N+1-docs/      # Documentation PR
            └── task-docs-update.md
```

---

## Core Files

### 1. plan.md - High-Level Implementation Plan

```markdown
# Implementation Plan: {Feature Name}

## Overview
- Tech stack decisions
- Implementation approach (backend-first, frontend-first, parallel)
- Execution model (linear sub-agents with verification)

## Stages

### Stage 1: {Stage Name}
| Task | Description | Dependencies | Estimated Complexity |
|------|-------------|--------------|---------------------|
| 1.1 | Task description | None | Low/Medium/High |
| 1.2 | Task description | 1.1 | Medium |

### Stage 2: {Stage Name}
...

## Summary
- Total stages: X
- Total tasks: Y
- Critical path: [list of blocking tasks]
```

### 2. pr-breakdown.md - PR-Sized Implementation Units

```markdown
# PR Breakdown: {Feature Name}

## Overview

| Total PRs | Backend PRs | Frontend PRs | E2E PR | Docs PR |
|-----------|-------------|--------------|--------|---------|
| {N} | {X} | {Y} | 1 | 1 |

## PR Sequence

### PR-1: {PR Title}
**Scope:** {What this PR implements}
**Type:** Backend / Frontend

| Task | Description |
|------|-------------|
| 1.1 | {Task description} |
| 1.2 | {Task description} |

**Tests Required:**
- Unit: {What unit tests cover}
- Integration: {What integration tests cover}

**Depends On:** None / PR-X

---

### PR-2: {PR Title}
...

---

### PR-N: E2E Tests
**Scope:** Happy path end-to-end tests
**Type:** Testing

| Test | User Flow |
|------|-----------|
| E2E-1 | {Flow description} |
| E2E-2 | {Flow description} |

**Based On:** acceptance-criteria.md (happy paths only)

**Depends On:** All implementation PRs

---

### PR-N+1: Documentation Update
**Scope:** Update lean documentation
**Type:** Documentation

| Update | File |
|--------|------|
| Status table | project/goals.md |
| IA entry | ia/{feature}.md |
| UX entry | ux/{feature}.md |
| UI entry | ui/{feature}.md |

**Depends On:** PR-N (E2E)
```

### 3. tracker.md - Session Continuity Tracker

```markdown
# Implementation Tracker: {Feature Name}

**Last Updated:** 2026-01-02T15:30:00Z
**Current PR:** 1
**Current Task:** 1.2

## Status Legend
- `pending` - Not started
- `in_progress` - Currently being implemented
- `ready_for_review` - Code and tests complete, awaiting human approval
- `completed` - Human approved/merged
- `blocked` - Waiting on dependency or issue

## PR Progress

| PR | Title | Status | Tasks Done | Notes |
|----|-------|--------|------------|-------|
| PR-1 | Entity + CRUD | in_progress | 1/3 | Working on service |
| PR-2 | Permissions | pending | 0/2 | - |
| PR-3 | Frontend List | pending | 0/4 | - |
| PR-N | E2E Tests | pending | 0/1 | - |
| PR-N+1 | Docs Update | pending | 0/1 | - |

## Current PR Tasks

### PR-1: Entity + CRUD
| Task | Status | Notes |
|------|--------|-------|
| 1.1 | completed | Schema created |
| 1.2 | in_progress | Service methods |
| 1.3 | pending | Controller |

## Session Log
| Session | Date | PR | Tasks Completed | Notes |
|---------|------|----|-----------------|-------|
| 1 | 2026-01-02 | PR-1 | 1.1 | Initial setup |
```

### 4. shared-context.md - Common Patterns & Naming

```markdown
# Shared Context: {Feature Name}

## Naming Conventions
| Type | Pattern | Example |
|------|---------|---------|
| Entity | PascalCase | `Organization` |
| DTO | PascalCase + Dto | `CreateOrganizationDto` |
| Service | PascalCase + Service | `OrganizationsService` |
| Controller | PascalCase + Controller | `OrganizationsController` |
| Guard | PascalCase + Guard | `AuthGuard` |
| Schema (Zod) | camelCase + Schema | `createOrganizationSchema` |

## Common Interfaces
```typescript
// User context available in all controllers
interface CurrentUser {
  id: string;
  email: string;
}

// Standard pagination
interface PaginationParams {
  page: number;
  limit: number;
}
```

## Shared Patterns
- Error handling: Use global exception filter
- Validation: Zod schemas with NestJS pipes
- Auth: Better Auth with session cookies

## File Locations
| Type | Location |
|------|----------|
| Database schemas | `apps/api/src/database/schema/` |
| DTOs | `apps/api/src/modules/{module}/dto/` |
| Guards | `apps/api/src/common/guards/` |
| Decorators | `apps/api/src/common/decorators/` |
```

### 5. Task Detail Files (tasks/pr-N/task-X.Y-name.md)

```markdown
# Task X.Y: {Task Name}

## Goal
{Clear, concise description of what this task accomplishes}

## Dependencies
- Task X.Z: {Why this dependency exists}
- External: {Any external dependencies}

## Files to Create/Modify

### Create
| File | Purpose |
|------|---------|
| `apps/api/src/config/configuration.ts` | Environment config loader |
| `apps/api/src/config/config.module.ts` | NestJS config module |

### Modify
| File | Changes |
|------|---------|
| `apps/api/src/app.module.ts` | Import ConfigModule |

## Entities/Classes/DTOs

### ConfigModule
```typescript
import { Module, Global } from '@nestjs/common';
import { ConfigModule as NestConfigModule } from '@nestjs/config';
import configuration from './configuration';

@Global()
@Module({
  imports: [
    NestConfigModule.forRoot({
      load: [configuration],
      isGlobal: true,
    }),
  ],
  exports: [NestConfigModule],
})
export class ConfigModule {}
```

### configuration.ts
```typescript
export default () => ({
  database: {
    url: process.env.DATABASE_URL,
  },
  auth: {
    secret: process.env.AUTH_SECRET,
  },
});
```

## Commands to Run
```bash
cd apps/api && pnpm add @nestjs/config
```

## Verification Steps
1. [ ] ConfigModule compiles without errors
2. [ ] DATABASE_URL is accessible via ConfigService
3. [ ] API starts successfully with `pnpm dev:api`

## Notes
- Reference: See shared-context.md for naming conventions
- Related: Task 1.3 will use ConfigService for database URL
```

---

## Workflow

```
1. LOAD SPECIFICATION
   ├── Read all docs from tasks/<folder>/
   ├── Parse requirements, data models, API contracts
   ├── Parse ia.md, ux.md, ui.md
   └── Identify acceptance criteria

2. CHECK FOR EXISTING IMPLEMENTATION
   ├── Look for implementation/ folder
   ├── If exists, read tracker.md
   └── Resume from last incomplete PR OR start fresh

3. CREATE IMPLEMENTATION STRUCTURE (if new)
   ├── Create implementation/ folder
   ├── Create plan.md with high-level stages
   ├── Create pr-breakdown.md with PR-sized units
   │   └── Include E2E and docs PRs
   ├── Create tracker.md with initial status
   ├── Create shared-context.md with naming/patterns
   └── Create task detail files for each PR

4. GET HUMAN APPROVAL ON PLAN
   ├── Present plan.md and pr-breakdown.md for review
   └── Wait for explicit approval before implementing

5. EXECUTE PRs (after plan approval)
   FOR each PR in pr-breakdown.md:
   │
   ├── Update tracker.md: PR → in_progress
   │
   ├── FOR each task in PR:
   │   ├── Implement code
   │   ├── Write unit tests
   │   └── Write integration tests
   │
   ├── Run all tests (must pass)
   │
   ├── Update tracker.md: PR → ready_for_review
   │
   ├── 🛑 STOP - Wait for human
   │   ├── Human reviews code
   │   ├── Human commits changes
   │   ├── Human creates/merges PR
   │   └── Human signals completion
   │
   ├── Update tracker.md: PR → completed
   │
   └── Proceed to next PR

6. E2E PR (after all implementation PRs)
   ├── Implement E2E tests (happy paths only)
   ├── Run E2E tests
   ├── 🛑 STOP - Wait for human approval

7. DOCS PR (after E2E PR)
   ├── Update project/goals.md status
   ├── Create/update ia/, ux/, ui/ docs
   ├── 🛑 STOP - Wait for human approval

8. COMPLETE
   └── Update tracker.md with final status
```

**IMPORTANT:** Claude does NOT perform git operations. Human handles all commits, branches, and PRs.

---

## Resuming a Session

When `--resume` is used or implementation/ folder exists:

1. Read `tracker.md` to find current state
2. Identify current PR and task status
3. Display session summary:
   ```
   Resuming implementation of auth-foundation...

   PR Progress: 2/6 PRs completed (33%)
   Current PR: PR-3 (Frontend List) - ready_for_review

   Status: Waiting for human to review/commit/merge PR-3

   Options:
   - If PR-3 was merged, say "PR-3 merged" to continue
   - If changes needed, describe what to fix
   ```
4. Resume based on human input

---

## Sub-Agent Instructions

### Implementation Sub-Agent Prompt Template

```
You are implementing Task {X.Y}: {Task Name} for PR-{N}

## Context
Read the following files:
1. tasks/{folder}/implementation/tasks/pr-{N}/task-{X.Y}-{name}.md
2. tasks/{folder}/implementation/shared-context.md
3. tasks/{folder}/implementation/pr-breakdown.md (for PR scope)

## Your Task
Implement exactly what is specified in the task file:
- Create/modify the files listed
- Follow the code patterns provided
- Use the naming conventions from shared-context.md
- Write unit tests for new code
- Write integration tests as specified

## Rules
- Only implement what's in the task file
- Do not add extra features or "improvements"
- Follow existing patterns in the codebase
- Do NOT perform any git operations
- Report any blockers or issues

## Output
When done, report:
1. Files created/modified
2. Tests written (unit + integration)
3. Any deviations from the plan (with reasons)
4. Ready for verification: yes/no
```

### Verification Sub-Agent Prompt Template

```
You are verifying Task {X.Y}: {Task Name}

## Context
Read: tasks/{folder}/implementation/tasks/pr-{N}/task-{X.Y}-{name}.md

## Your Task
Execute each verification step from the task file:
1. {Verification step 1}
2. {Verification step 2}
...

Run all tests:
- Unit tests must pass
- Integration tests must pass

## Output
For each step, report:
- PASS or FAIL
- Evidence (command output, file exists, etc.)
- If FAIL: specific issue found

## Final Verdict
- ALL_PASSED: Task is complete
- FAILED: List failures, do not proceed
```

---

## Progress Tracking

Uses both:
1. **tracker.md** - Persistent file for session continuity
2. **TodoWrite tool** - Real-time Claude Code tracking

Keep both in sync:
```
tracker.md status     →  TodoWrite status
pending               →  pending
in_progress           →  in_progress
ready_for_review      →  in_progress (note: awaiting human)
completed             →  completed
blocked               →  (not shown, mention in notes)
```

---

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Task folder not found | Error with available folders list |
| Implementation folder exists | Ask: resume or start fresh? |
| Missing prerequisite | Mark PR as blocked, report to human |
| Tests fail | Keep PR in_progress, report failures, fix before marking ready |
| Human requests changes | Update code, re-run tests, mark ready_for_review again |
| Sub-agent error | Log error, pause for human decision |

---

## Example Session

```
User: /implement-feature 2026_0101_151735_workspaces

Claude: Found existing implementation folder. Reading tracker...

PR Progress: 2/6 PRs completed (33%)
Current PR: PR-3 (Workspace Frontend List) - ready_for_review

Status: Waiting for human to review/commit/merge PR-3

If PR-3 was merged, say "PR-3 merged" to continue.
If changes needed, describe what to fix.

User: PR-3 merged

Claude: Great! Updating tracker...

[Updates tracker.md: PR-3 → completed]

Starting PR-4: Workspace Create/Edit Forms

[Updates tracker.md: PR-4 → in_progress]

Implementing tasks for PR-4:
- Task 4.1: CreateWorkspaceForm component
- Task 4.2: EditWorkspaceForm component
- Task 4.3: Form validation with Zod
- Task 4.4: Unit and integration tests

[Implements all tasks]

All tests passing:
✓ 12 unit tests
✓ 4 integration tests

[Updates tracker.md: PR-4 → ready_for_review]

PR-4 is ready for your review. Files changed:
- apps/dashboard/src/features/workspaces/components/CreateWorkspaceForm.tsx
- apps/dashboard/src/features/workspaces/components/EditWorkspaceForm.tsx
- apps/dashboard/src/features/workspaces/components/__tests__/...

Please review, commit, and merge when ready.
```

---

## Feedback Log

| Date | Feedback | Incorporated Change |
|------|----------|---------------------|
| 2026-01-02 | Need session continuity | Added tracker.md and implementation folder structure |
| 2026-01-02 | Context preservation | Added shared-context.md and task detail files |
| 2026-01-06 | PR-based workflow | Added pr-breakdown.md, PR-sized task groupings |
| 2026-01-06 | Human approval gates | Added ready_for_review status, stop points between PRs |
| 2026-01-06 | Human manages git | Removed all git operations from Claude's workflow |
| 2026-01-06 | E2E and docs as PRs | E2E and docs tasks planned upfront in pr-breakdown.md |

---

## Related Skills

| Skill | Relationship |
|-------|--------------|
| `/design-feature` | Creates specifications this skill implements |
| `SkillForge` | Created this skill |

---

## Extension Points

1. **Custom task templates**: Add templates for specific task types
2. **Validation scripts**: Add domain-specific validators
3. **CI integration**: Trigger tests after each stage
4. **Parallel execution**: Future support for independent tasks in parallel
5. **Progress visualization**: Generate progress charts from tracker.md
