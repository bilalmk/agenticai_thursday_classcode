from agents import Agent
from my_config.gemini_confg import MODEL
from my_tool.my_tools import plus,subtract
from instruction.dynamic_instruction import dynamic_instruction


assistant = Agent(
    name="Assistant",
    instructions=dynamic_instruction,
    model=MODEL,
    tools=[subtract]
)

# print(assistant.tools)