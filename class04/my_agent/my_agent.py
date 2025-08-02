from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tool.my_tools import multiply,plus

agent = Agent(name="Ratan lal", instructions="You are helpful assistant", model=MODEL,tools=[multiply,plus] , tool_use_behavior="run_llm_again")

