from agents import  Runner, set_tracing_disabled
from my_agent.agent import agent
from data.user_data import user1

set_tracing_disabled(True)

res = Runner.run_sync(starting_agent=agent, input="User ki age batao?",context=user1)

print(res.final_output)