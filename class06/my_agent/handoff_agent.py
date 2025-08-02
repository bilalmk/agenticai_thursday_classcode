from agents import Agent, handoff, function_tool, RunContextWrapper
from my_confg.gemini_confg import MODEL
from agents.extensions import handoff_filters
from data.user_data import UserData

@function_tool
async def fetch_weather(city: str):
    return f"the weather in {city} is sunny with 45C"

next_js_assistant =Agent(
    name="Next js Assistant",
    instructions="You are helpful next js assitant",
    model=MODEL, 
)

python_assistant = Agent(
    name="Python Assistant",
    instructions="you are helpful python assistant.",
    model=MODEL, 
)

def on_handoff_function(ctx:RunContextWrapper[UserData]):
    print(f"Hi kem cho! {ctx.context.name}")

# Agent NAme = Python Assistant
# hand off name = transfer_to_python_assisant
python_handoff = handoff(
    agent=python_assistant,
    tool_name_override="handover_to_python_assisant",
    on_handoff=on_handoff_function,
    input_filter=handoff_filters.remove_all_tools
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are helpfull assiatnt handoff the request to the correct agent accoriding to the query",
    handoffs=[next_js_assistant,python_handoff],
    tools=[fetch_weather],
    model=MODEL, 
    )









