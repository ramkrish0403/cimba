import json

from agents import RunContextWrapper, function_tool

from src.features.simple_chat_agent.context import SimpleChatContext


@function_tool
def get_session_metadata(
    wrapper: RunContextWrapper[SimpleChatContext],
) -> str:
    """
    Get the session metadata from the context.

    Returns:
        str: The session metadata as a JSON string.
    """
    return json.dumps(wrapper.context.metadata, indent=2)


@function_tool
def set_session_metadata(
    wrapper: RunContextWrapper[SimpleChatContext],
    key: str,
    value: str,
) -> str:
    """
    Set a key-value pair in the session metadata.

    Args:
        key: The metadata key.
        value: The metadata value.

    Returns:
        str: Success message.
    """
    wrapper.context.metadata[key] = value
    return f"Metadata key '{key}' set successfully."
