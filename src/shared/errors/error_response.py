from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    error: str
    message: str
    details: list[dict[str, Any]] | None = None
