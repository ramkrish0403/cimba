import json
import os
from typing import Any

from dataclasses_json import DataClassJsonMixin
from pydantic import Field
from pydantic.dataclasses import dataclass as pydantic_dataclass

SESSIONS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ".sessions"
)


@pydantic_dataclass(kw_only=True)
class SimpleChatContext(DataClassJsonMixin):
    session_id: str = ""
    system_prompt: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

    @staticmethod
    def _get_session_dir(session_id: str) -> str:
        return os.path.join(SESSIONS_DIR, session_id)

    @staticmethod
    def _get_context_path(session_id: str) -> str:
        return os.path.join(SESSIONS_DIR, session_id, "context.json")

    @staticmethod
    def get_db_path(session_id: str) -> str:
        return os.path.join(SESSIONS_DIR, session_id, "chat.db")

    def save(self) -> None:
        session_dir = self._get_session_dir(self.session_id)
        os.makedirs(session_dir, exist_ok=True)
        with open(self._get_context_path(self.session_id), "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @staticmethod
    def load(session_id: str) -> "SimpleChatContext":
        context_path = SimpleChatContext._get_context_path(session_id)
        if not os.path.exists(context_path):
            return SimpleChatContext(session_id=session_id)
        with open(context_path, "r") as f:
            data = json.load(f)
        return SimpleChatContext.from_dict(data)
