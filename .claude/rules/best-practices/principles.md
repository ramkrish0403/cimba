---
description: Core development principles for Cimba
---

# Development Principles

## SOLID

| Principle | Description |
|-----------|-------------|
| **SRP** | One reason to change per class/function |
| **OCP** | Open for extension, closed for modification |
| **LSP** | Subtypes must be substitutable for their base types |
| **ISP** | Prefer small, specific interfaces over large ones |
| **DIP** | Depend on abstractions, not concretions |

## DRY (Don't Repeat Yourself)

- Extract shared logic to utils or shared packages
- If you copy-paste code, consider abstraction
- But avoid premature abstraction - wait for 3 occurrences

## KISS (Keep It Simple)

- Choose the simplest solution that works
- Prefer clear code over clever code
- Avoid unnecessary complexity

## YAGNI (You Aren't Gonna Need It)

- Don't build features speculatively
- Implement only what's currently needed
- Future requirements can be added when they become real

## Vertical Slice Architecture

Organize code by **feature**, not by technical layer. Each feature is a self-contained slice with all its own layers co-located together.

### Feature Module Structure (NestJS-style)

```
src/
  features/
    <feature>/
      dto/                  # Data Transfer Objects (request/response shapes)
        create-<feature>.dto.ts
        update-<feature>.dto.ts
      entities/             # Domain entities / ORM models
        <feature>.entity.ts
      <feature>.controller.ts   # HTTP layer (routes, validation, auth guards)
      <feature>.service.ts      # Business logic
      <feature>.repository.ts   # Data access / persistence
      <feature>.module.ts       # NestJS module wiring
      <feature>.spec.ts         # Tests for the feature
  shared/                   # Cross-cutting concerns used by multiple features
    dto/
    entities/
    utils/
```

### Rules

- **Each feature owns its full stack**: DTOs, entities, controller, service, repository, and module live together
- **No cross-feature imports of internal files**: Features communicate through their module's exported service, never by importing another feature's repository or entity directly
- **DTOs are the API contract**: Controllers accept and return DTOs, never raw entities
- **Entities are the persistence contract**: Repositories deal in entities, services map between entities and DTOs
- **Services contain business logic**: Controllers stay thin (validate + delegate), repositories stay thin (query + persist)
- **Shared code requires justification**: Only extract to `shared/` when used by 3+ features (DRY rule of three)

## Code Quality

- **Test behavior, not implementation**: Tests should survive refactoring
- **Co-locate related code**: Feature modules keep related files together
- **Clear naming**: Functions as verbs, variables as nouns

## When Adding Features

1. Check if similar functionality exists
2. Follow existing patterns in the codebase
3. Create a new vertical slice under `src/features/<feature>/` with dto, entity, controller, service, repository, and module
4. Keep changes focused and minimal
5. Don't refactor unrelated code

## Plan Validation

Before finalizing any implementation plan, verify it follows these principles.
