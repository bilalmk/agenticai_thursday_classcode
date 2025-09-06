from agents import Agent, function_tool


@function_tool
def get_weather(city: str) -> str:
    "return the weather of provided city"
    return f"{city}:35 degree centigrade"


weather_agent: Agent = Agent(
    name="WeatherAgent",
    instructions="You are a weather agent, provide the weather of city",
    handoff_description="This is a weather agent",
    tools=[get_weather],
)
