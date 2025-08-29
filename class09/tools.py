from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    ToolsToFinalOutputFunction,
    function_tool,
    set_tracing_disabled,
    ToolsToFinalOutputResult,
    set_tracing_export_api_key,
    ModelSettings,
    FunctionTool,
)

from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os

from pydantic import BaseModel

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")

set_tracing_export_api_key(str(api_key))

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)

model = OpenAIChatCompletionsModel(model=str(model_name), openai_client=client)



@function_tool
def get_weather(city: str):
    "get the weather of provided city"
    return f"the temperature of {city} is 35 degree and mostly sunny"

agent = Agent(
    name="General Purpose Agent",
    instructions="You are an helpful agent",
    model=model,
    tools=[get_weather],
)


async def main():
    result = await Runner.run(agent, "weather of karachi")
    print(result.final_output)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
