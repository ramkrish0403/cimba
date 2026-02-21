# 0002 - Global Error Handling

**Status:** accepted
**Date:** 2026-02-21

## Context
Endpoints returned raw FastAPI defaults (HTML error pages, inconsistent JSON). We needed consistent, structured JSON error responses across all endpoints.

## Decision
Add shared error handling in `src/shared/errors/` with a Pydantic `ErrorResponse` model, an `AppError` exception hierarchy, and global exception handlers registered on the FastAPI app. New error types are added by subclassing `AppError` (OCP).

## Consequences
- All errors return `{error, message, details}` JSON
- New exceptions only require a subclass with `status_code` and `error_code` — no handler changes
- Unhandled exceptions are caught and logged without leaking stack traces
- Validation errors include per-field details
