from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled,
    set_default_openai_api,
    set_default_openai_client,
)
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os


load_dotenv(override=True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
set_tracing_disabled(True)
set_default_openai_client(client)
set_default_openai_api("chat_completions")


agent: Agent = Agent(
    name="Math Agent",
    instructions="""
    - You are helpful math agent
    - you can solve complex math questions and expression
    - DO NOT answer if request is not about Math questions
    - DO NOT generate answer on yourself if question are not about MATH
    - You can simply refuse the answer if you don't know
    """,
    model="gemini-2.0-flash",
)

prompt = input("Enter your question")
result = Runner.run_sync(agent, prompt)
print(result.final_output)
