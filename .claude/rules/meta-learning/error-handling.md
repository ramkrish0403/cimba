Shared error handling lives in `src/shared/errors/`. Subclass `AppError` with `status_code` and `error_code` class attributes for new error types — no handler changes needed.
