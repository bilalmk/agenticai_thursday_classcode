from agents import Agent
from my_confg.gemini_confg import MODEL

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


triage_agent = Agent(
    name="Triage Agent",
    instructions="You are helpfull assiatnt handoff the request to the correct agent accoriding to the query",
    handoffs=[next_js_assistant,python_assistant],
    model=MODEL, 
    )









