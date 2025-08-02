from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tool.weather_tool import fetch_weather

weather_agent = Agent(
 name="Weather Assistant",
 instructions="You are helpful weather assistant by calling fetch_weather tool",
 model=MODEL,
 tools=[fetch_weather]
)

