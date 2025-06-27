from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, RunConfig
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os

set_tracing_disabled(True)
load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_PATH")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
gemini_model = OpenAIChatCompletionsModel(openai_client=gemini_client, model=str(gemini_model_name))

openai_api_key = os.getenv("GEMINI_API_KEY")
openai_base_url = os.getenv("GEMINI_BASE_PATH")
openai_model_name = os.getenv("GEMINI_MODEL_NAME")


# openai_client = AsyncOpenAI(api_key=openai_api_key, base_url=openai_base_url)
# openai_model = OpenAIChatCompletionsModel(openai_client=openai_client, model=str(openai_model_name))

math_agent: Agent = Agent(
    name="Math Agent",
    instructions="""
    - You are helpful math agent
    - you can solve complex math questions and expression
    - DO NOT answer if request is not about Math questions
    - DO NOT generate answer on yourself if question are not about MATH
    - You can simply refuse the answer if you don't know
    """,
    #model=gemini_model,
)

physics_agent: Agent = Agent(
    name="Physics Agent",
    instructions="""
    - You are helpful Physics agent
    - you can solve complex Physics numerical and explain theory
    - DO NOT answer if request is not about Physics questions
    - DO NOT generate answer on yourself if question are not about Physics
    - You can simply refuse the answer if you don't know
    """,
    #model=gemini_model,
)

config = RunConfig(model=gemini_model)

prompt = input("Enter your question")
result = Runner.run_sync(physics_agent, prompt, run_config=config)
print(result.final_output)
