from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled,
    OpenAIResponsesModel,
    function_tool,
    set_tracing_export_api_key,
    ModelSettings
)
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os


load_dotenv(override=True)
#gemini_api_key = os.getenv("GEMINI_API_KEY")
#gemini_base_url = os.getenv("GEMINI_BASE_PATH")
#gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

#set_tracing_disabled(True)
#set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))
#client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
#model = OpenAIChatCompletionsModel(openai_client=client, model=str(gemini_model_name))


@function_tool(name_override="get_weather_info", description_override="get weather info for provided city")
def get_weather(city: str):
    """weather function"""
    print("get_weather")
    return f"{city}:35"

@function_tool
def add(a:int, b:int):
    "add two numbers and return value"
    print("add tool")
    return a+b

agent: Agent = Agent(
    name="Helpful General Agent",
    instructions="""
    You are a helpful agent
    """,
    #model="gpt-4o-mini",
    model_settings=ModelSettings(tool_choice="auto"),
    tools=[get_weather, add]
)

#print(agent.tools[0])


prompt = input("Enter your question : ")
result = Runner.run_sync(agent, prompt)
print(result.final_output)


