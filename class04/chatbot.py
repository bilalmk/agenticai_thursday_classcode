import chainlit as cl
from agents import Runner
from my_agent.my_agent import agent

@cl.on_message
async def main(msg:cl.Message):
    prompt = msg.content

    res = Runner.run_sync(agent, input=prompt)

    await cl.Message(content=res.final_output).send()
