import asyncio
from typing import Any
from agents import (
    Agent,
    HandoffCallItem,
    HandoffInputData,
    HandoffOutputItem,
    MessageOutputItem,
    RunConfig,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    ToolCallItem,
    ToolCallOutputItem,
    handoff,
    ModelSettings,
)
from my_config import model
from my_agents.weather_agent import weather_agent
from my_agents.flight_agent import flight_agent
from my_agents.hotel_agent import hotel_agent
from agents.extensions import handoff_filters


def filter_handoff(input_data: HandoffInputData) -> HandoffInputData:
    input_data = handoff_filters.remove_all_tools(input_data)
    history = input_data.input_history[-2:]
    return HandoffInputData(
        input_history=history,
        pre_handoff_items=input_data.pre_handoff_items,
        new_items=input_data.new_items,
    )


def enabled_handoff(ctx: RunContextWrapper[Any], agent: Agent) -> bool:
    return True


triage_agent: Agent = Agent(
    name="TriageAgent",
    instructions="""
 You are a triage agent, you can handoff to weather,flight or hotel agent
 if user asking for. You can answer your self if not handoff to agents
 """,
    handoffs=[
        handoff(
            weather_agent,
            tool_name_override="weather_handoff",
            input_filter=filter_handoff,
            is_enabled=enabled_handoff,
        ),
        hotel_agent,
        flight_agent,
    ],
)

weather_agent.handoffs.append(triage_agent)
hotel_agent.handoffs.append(triage_agent)
flight_agent.handoffs.append(triage_agent)


async def main():
    starting_agent = triage_agent
    data_input: list[TResponseInputItem] = []
    while True:
        msg = input("Enter your query : ")
        print("\n\n")
        data_input.append({"role": "user", "content": msg})

        if msg == "exit":
            break

        result = await Runner.run(
            starting_agent,
            input=data_input,
            run_config=RunConfig(model=model),
        )
        # print(result.final_output)
        for item in result.new_items:
            if isinstance(item, ToolCallItem):
                print(f"tool call : {item.raw_item.name}")
            elif isinstance(item, ToolCallOutputItem):
                print(f"tool output : {item.output}")
            elif isinstance(item, MessageOutputItem):
                print(f"final output from agent : {item.agent.name} is : {item.raw_item.content[0].text}")
            elif isinstance(item, HandoffCallItem):
                print(f"hand off start for : {item.raw_item.name}")
            elif isinstance(item, HandoffOutputItem):
                print(
                    f"handoff complete from {item.source_agent.name} to {item.target_agent.name}"
                )
            else:
                print("nothing")
            print("================================================")
        starting_agent = result.last_agent
        data_input = result.to_input_list()
        result.last_response_id


asyncio.run(main())
