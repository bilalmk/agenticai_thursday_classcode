import chainlit as cl
from main import math_agent
from agents import Runner

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="Bhai jan sochne do....").send()
    # my rompt 
    prompt = message.content
    # agent get
    result = Runner.run_sync(math_agent, prompt)
    await cl.Message(content=f"Ai-response: {result.final_output}").send()