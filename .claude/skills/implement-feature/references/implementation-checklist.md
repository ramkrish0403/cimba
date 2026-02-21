# Implementation Checklist

Use this checklist when implementing a feature to ensure completeness.

---

## Pre-Implementation

- [ ] Read all specification documents in task folder
- [ ] Verify prerequisites exist
- [ ] Identify reusable components in `packages/ui`
- [ ] Check existing patterns in `features/`
- [ ] Create implementation plan
- [ ] Get human approval for plan

---

## Feature Module Setup

- [ ] Create feature directory under `features/{feature-name}/`
- [ ] Create subdirectories:
  - [ ] `api/`
  - [ ] `components/`
  - [ ] `hooks/`
  - [ ] `stores/` (if needed)
  - [ ] `types/`
  - [ ] `schemas/`
  - [ ] `utils/`
- [ ] Create `index.ts` for public exports

---

## Data Layer

- [ ] Create Zod schemas from `data-models.md`
- [ ] Export inferred TypeScript types
- [ ] Add validation helpers if complex rules exist
- [ ] Test schemas with edge case data

---

## API Layer

- [ ] Check if Orval-generated hooks exist
- [ ] Create custom hooks wrapping generated hooks (if needed)
- [ ] Implement query key patterns
- [ ] Add optimistic update logic for mutations
- [ ] Handle error states
- [ ] Add loading states

---

## UI Components

For each component:
- [ ] Use shadcn/ui primitives where applicable
- [ ] Follow component hierarchy from `ui.md`
- [ ] Implement user flows from `ux.md`
- [ ] Follow navigation structure from `ia.md`
- [ ] Implement responsive behavior
- [ ] Add accessibility attributes
- [ ] Handle loading, error, empty states
- [ ] Use design tokens from `ui-design-guide.md`

---

## State Management

- [ ] Determine state type (server vs client)
- [ ] For server state: use TanStack Query
- [ ] For client state: use Zustand if needed
- [ ] Create selectors for derived state
- [ ] Implement persistence if required (user preferences)

---

## Routing

If feature has routes:
- [ ] Create route files in `app/routes/`
- [ ] Define search params schema with Zod
- [ ] Implement route loaders for data prefetching
- [ ] Update navigation with type-safe `<Link>`
- [ ] Handle protected routes with auth checks

---

## Integration

- [ ] Export public API from `index.ts`
- [ ] Only export what other features need
- [ ] Keep internal implementation private
- [ ] Verify imports work from other features

---

## Quality Checks

- [ ] Run `tsc --noEmit` - no TypeScript errors
- [ ] Run linter - no warnings
- [ ] Check bundle size impact
- [ ] Verify no circular dependencies

---

## Acceptance Criteria Validation

For each criterion in `acceptance-criteria.md`:
- [ ] AC-001: {description} - Verified
- [ ] AC-002: {description} - Verified
- [ ] ... continue for all criteria

---

## Documentation

- [ ] Update README.md status in task folder
- [ ] Add JSDoc to complex functions
- [ ] Document any deviations from specification
- [ ] Note any discovered issues or improvements

---

## Post-Implementation

- [ ] Run validation script
- [ ] Report completion status
- [ ] Identify follow-up tasks if any
- [ ] Update Feedback Log if learnings apply
