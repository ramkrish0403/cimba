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

## Code Quality

- **Test behavior, not implementation**: Tests should survive refactoring
- **Co-locate related code**: Feature modules keep related files together
- **Clear naming**: Functions as verbs, variables as nouns

## When Adding Features

1. Check if similar functionality exists
2. Follow existing patterns in the codebase
3. Keep changes focused and minimal
4. Don't refactor unrelated code

## Plan Validation

Before finalizing any implementation plan, verify it follows these principles.
