from agents import  Runner, set_tracing_disabled
from my_agent.my_agents import agent
from my_agent.handoff_agent import triage_agent
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

set_tracing_disabled(True)

# res = Runner.run_sync(starting_agent=agent,input="Plus akro 100 me 200.")
# res= Runner.run_sync(
#     starting_agent=triage_agent,
#     input="mujhe next js ki routing k hawale se help chaiye"

#     )

async def main():
    res= Runner.run_streamed(starting_agent=triage_agent, input="what is nextjs in one line.")

    async for event in res.stream_events():
        # print(event.type)
        if event.type == "raw_response_event" and isinstance(event.data,ResponseTextDeltaEvent ):
            print(event.data.delta)



asyncio.run(main())
# await main()
# Runner.run_sync
# Runner.run
# Runner.run_streamed
# print("Last Agent>>>>>",res.last_agent)
# print("Final Output",res.final_output)


