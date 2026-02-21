import logging
from datetime import datetime, timezone

from agents import Agent, ModelSettings, Runner, SQLiteSession, WebSearchTool
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent

from src.features.simple_chat_agent.context import SimpleChatContext
from src.features.simple_chat_agent.tools.context_tools import (
    get_session_metadata,
    get_system_prompt,
    set_session_metadata,
)

logger = logging.getLogger(__name__)


def get_chat_agent(
    context: SimpleChatContext,
    model: str = "gpt-4.1-mini",
) -> Agent[SimpleChatContext]:
    current_time_iso = datetime.now(timezone.utc).isoformat()

    system_prompt = f"""
Current Time: {current_time_iso}

You are a helpful chat assistant. You can answer questions, help with tasks, and search the web for up-to-date information.

# Your Capabilities:
- Answer general knowledge questions
- Help with writing, analysis, and brainstorming
- Search the web for current information when needed
- Access and manage conversation context

# Instructions:
- Be concise and helpful in your responses
- Use web search when the user asks about current events or needs up-to-date information
- Use markdown formatting when appropriate
- If you don't know something, say so honestly

{f"Additional instructions: {context.system_prompt}" if context.system_prompt else ""}
"""

    agent = Agent[SimpleChatContext](
        name="Simple Chat Agent",
        instructions=system_prompt,
        model=model,
        model_settings=ModelSettings(
            parallel_tool_calls=True,
        ),
        tools=[
            WebSearchTool(),
            get_session_metadata,
            set_session_metadata,
        ],
    )
    return agent


async def execute_chat_agent(
    user_message: str,
    session_id: str = "default",
    system_prompt: str = "",
    model: str = "gpt-4.1-mini",
    enable_streaming: bool = False,
) -> str:
    context = SimpleChatContext.load(session_id)
    if system_prompt:
        context.system_prompt = system_prompt

    agent = get_chat_agent(context=context, model=model)
    db_path = SimpleChatContext.get_db_path(session_id)
    session = SQLiteSession(db_path=db_path, session_id=session_id)

    if not enable_streaming:
        result = await Runner.run(
            starting_agent=agent,
            input=user_message,
            session=session,
            context=context,
            max_turns=30,
        )
        context.save()
        return result.final_output

    result = Runner.run_streamed(
        starting_agent=agent,
        input=user_message,
        session=session,
        context=context,
        max_turns=30,
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event":
            if isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)

    print()
    context.save()
    return result.final_output
