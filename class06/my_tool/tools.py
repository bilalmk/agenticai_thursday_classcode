from agents import function_tool, RunContextWrapper
from data.user_data import UserData

@function_tool
def plus(ctx:RunContextWrapper[UserData],n1,n2):
    print("Plus tool fire ----->")
    print(ctx.context.name)
    return f"your answer is {n1+n2}"

@function_tool
def get_user_age(ctx:RunContextWrapper[UserData]):
    print("User age tool fire ----->")
    print(ctx.context.name)
    return f"{ctx.context.name} age is {ctx.context.age}"
