from agents import Runner, set_tracing_disabled
from my_agent.assistant import assistant


set_tracing_disabled(True)

res = Runner.run_sync(
    starting_agent=assistant, 
    input="10-7=?",
    context={"name":"Atma ram", "age":13, "role":"teacher"}
    )

print(res.final_output)