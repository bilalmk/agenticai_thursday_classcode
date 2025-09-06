from agents import Agent, function_tool


@function_tool
def search_hotel(city: str) -> str:
    "search hotel in city"
    return """
    - PC hotel, 1 night fare 28000, single bed, free wifi, free parking
    - MovenPick, 1 night fare 20000, single bed, free wifi, free parking
"""


hotel_agent: Agent = Agent(
    name="HotelAgent",
    instructions="You are a hotel agent, provide a list of hotels in city",
    handoff_description="This is a hotel agent, search the best and cheap hotel in town",
    tools=[search_hotel],
)
