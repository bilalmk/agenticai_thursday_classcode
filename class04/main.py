from agents import Runner, set_tracing_disabled
from my_agent.weather_agent import weather_agent


set_tracing_disabled(True)
result = Runner.run_sync(starting_agent=weather_agent, input="What is weather in multan?")
print("result", result.final_output)


















# from agents import Runner, set_tracing_disabled, enable_verbose_stdout_logging
# from my_agent.my_agent import agent

# set_tracing_disabled(True)
# # enable_verbose_stdout_logging()

# res = Runner.run_sync(agent, input="plus kare 10 me 20")

# print(res.final_output)