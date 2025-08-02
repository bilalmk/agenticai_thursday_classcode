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
    SQLiteSession,
)
from agents.agent import StopAtTools
from agents.tool import FunctionToolResult
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

from pydantic import BaseModel
import asyncio

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

agent = Agent(
    name="General Purpose Agent",
    instructions="You are an helpful agent",
    model=model,
)


async def main():
    prompt = input("Enter your question : ")
    result = await Runner.run(agent, prompt)
    print(result.final_output)

    prompt = input("\n\nEnter your question : ")
    new_prompt = result.to_input_list() + [{"role": "user", "content": prompt}]
    result = await Runner.run(agent, new_prompt)
    print(result.final_output)

    # print(result.final_output)
    # print(result.to_input_list())


async def main_new():
    my_session = SQLiteSession("mysession_123", "my_conversation.db")
    prompt = input("Enter your question : ")
    result = await Runner.run(agent, prompt, session=my_session)
    print(result.final_output)

    prompt = input("\n\nEnter your question : ")
    result = await Runner.run(agent, prompt, session=my_session)
    print(result.final_output)


asyncio.run(main_new())
