class AppError(Exception):
    status_code: int = 500
    error_code: str = "internal_error"

    def __init__(self, message: str = "Internal server error"):
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):
    status_code: int = 404
    error_code: str = "not_found"

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message)


class ConflictError(AppError):
    status_code: int = 409
    error_code: str = "conflict"

    def __init__(self, message: str = "Resource conflict"):
        super().__init__(message)
