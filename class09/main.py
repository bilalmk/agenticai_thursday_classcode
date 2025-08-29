from agents import (
    Agent,
    ModelSettings,
    OpenAIChatCompletionsModel,
    Runner,
    function_tool,
    set_tracing_export_api_key,
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
def get_weather(city: str) -> str:
    "return the weather of provided city"
    return f"{city}:35 degrees"


@function_tool
def get_news(topic: str) -> str:
    "return the news about the provided topic"
    return "pakistan flood"


agent = Agent(
    "helpfulAssistant",
    instructions="You are a helpful assistant",
    model=model,
    model_settings=ModelSettings(temperature=0.9, top_p=0.1),
    tools=[get_weather, get_news],
)

new_agent = agent.clone(name="NewAgent")
print(id(agent))
print(id(new_agent))

# print("old_agent : ", agent)
# print("\n\n===========================================\n\n")
# print("new Agent : ", new_agent)


# a = [1, 2]
# b = a
# print(f"a : {id(a)}")
# print(f"b : {id(b)}")
# b[0] = 3
#print(f"a : {a}")
#print(f"b : {b}")

# a = 10
# b = a
# b = 20

# print(f"a : {id(a)}")
# print(f"b : {id(b)}")
# print(agent.model_settings)
# print("====================================")

# ms = ModelSettings(temperature=0.5)
# ms = agent.model_settings.resolve(override=ModelSettings(temperature=0.5))
# print(ms)


# result = Runner.run_sync(
#     agent,
#     "write a quote about software development",
# )

# cat is sit on
# mat   40%
# chair 30%
# table 20%
# banana 10%
# print(result.final_output)
