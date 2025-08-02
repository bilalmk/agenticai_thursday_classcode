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
from agents.agent import StopAtTools
from agents.tool import FunctionToolResult
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

from pydantic import BaseModel

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")

# set_tracing_disabled(True)
set_tracing_export_api_key(str(api_key))

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)

model = OpenAIChatCompletionsModel(model=str(model_name), openai_client=client)


class Weather(BaseModel):
    city: str


# async def get_wether_func(ctx, city:Weather):
#     print("test")
#     return {"city": city, "temprature": "35"}


# tool = FunctionTool(
#     name="get_weather",
#     description="get weather of city",
#     on_invoke_tool=get_wether_func,
#     params_json_schema=Weather.model_json_schema(),
#     is_enabled=True,
# )

@function_tool
def get_weather(city:str):
    "get the weather of provided city"
    print("test")
    return {"city": city, "temprature": "35"}

agent = Agent(
    name="General Purpose Agent",
    instructions="You are an helpful agent",
    model=model,
    tools=[get_weather],
)


async def main():
    #prompt = input("Enter your question : ")
    #result = await Runner.run(agent, prompt)
    #print(result.final_output)
    print(agent.tools)
    print(Weather.model_json_schema())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

# FunctionTool(
#     name='get_weather', 
#     description='', 
#     params_json_schema={'properties': {'city': {'title': 'City'}}, 'required': ['city'], 'title': 'get_weather_args', 'type': 'object', 'additionalProperties': False}, 
#     on_invoke_tool=<function function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x00000162F310FC40>, 
#     strict_json_schema=True, 
#     is_enabled=True)