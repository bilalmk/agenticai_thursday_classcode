from agents import RunContextWrapper

def dynamic_instruction(ctx:RunContextWrapper,agent):
    # print(agent)
    return f"User name {ctx.context["name"]},  you are helpful assistant"


async def en(ctx:RunContextWrapper,agent):
    if ctx.context["age"] >= 18:
        return True
    return False