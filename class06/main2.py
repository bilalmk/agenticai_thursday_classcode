from agents import  Runner, set_tracing_disabled, ItemHelpers,HandoffInputData
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
    # res = Runner.run_streamed(
    #     starting_agent=triage_agent,
    #     input="what is nextjs")
    
    # async for event in res.stream_events():
    #     if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
    #     #    print(event.data.delta)
    #        continue
    #     elif event.type == "agent_updated_stream_event":
    #         continue
    #     elif event.type == "run_item_stream_event":
    #         if event.item.type == "message_output_item":
    #             # print(event.item.raw_item.content[0].text)
    #             print(ItemHelpers.text_message_output(event.item))

    result =await Runner.run(
        starting_agent=triage_agent,con
        input="what is the weather in karachi and What is python variables." ) 
    # print("Last Agent",result.last_agent)
    print("Result",result.final_output)


asyncio.run(main())
# await main()
# Runner.run_sync
# Runner.run
# Runner.run_streamed
# print("Last Agent>>>>>",res.last_agent)
# print("Final Output",res.final_output)


