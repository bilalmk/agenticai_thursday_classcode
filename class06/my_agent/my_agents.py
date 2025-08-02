from agents import Agent, ModelSettings
from agents.agent import StopAtTools
from my_confg.gemini_confg import MODEL
from my_tool.my_tools import plus,subtract


math_agent = Agent(name="Gulzari lal", 
              instructions="You are my assistant.", 
              model=MODEL, 
              tools=[plus,subtract], 
              model_settings=ModelSettings(tool_choice="required")
              )

agent = Agent(name="Ratan lal", 
              instructions="You are my assistant.", 
              model=MODEL, 
              tools=[math_agent.as_tool(tool_name="math_teacher",tool_description="you are math teacher.")]
              )



