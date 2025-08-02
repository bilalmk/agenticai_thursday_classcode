from agents import function_tool, RunContextWrapper, FunctionTool
from tool_type.subtract_tool import SubtractSchema
from instruction.dynamic_instruction import en


async def subtract_func(ctx:RunContextWrapper,arg):
    print("subtract tool ----->")
    obj = SubtractSchema.model_validate_json(arg)
    return f"you answer is {obj.n1 - obj.n2}"


subtract = FunctionTool(
    name="subtract",
    description="Subtract function.",
    params_json_schema=SubtractSchema.model_json_schema(),
    on_invoke_tool=subtract_func,
    is_enabled=en
)




@function_tool(description_override="Hello description", name_override="fun_plus",is_enabled=False)
def plus(ctx:RunContextWrapper,n1,n2):
    """plus function"""
    print("Plus tool fire ---->")
    print("ctx ----->",ctx.context["name"])
    return f"you answer is {n1+n2}"

