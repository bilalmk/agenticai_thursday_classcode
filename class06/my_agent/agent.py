from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tool.tools import plus,get_user_age


agent = Agent(name="Assistant", 
              instructions="You are my assistant.", 
              model=MODEL, 
              tools=[plus,get_user_age]
            )



