from agents import Agent, function_tool


@function_tool
def search_flight(from_city: str, to_city: str, date: str):
    return f"flight PK201 available from {from_city} to {to_city} and fare is 15000 PKR"


flight_agent: Agent = Agent(
    name="FlightAgent",
    instructions="You are a flight agent, search cheap and best flight between 2 cities",
    handoff_description="This is a flight agent, provide flight on specific date",
    tools=[search_flight],
)
