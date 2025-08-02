from agents import function_tool

@function_tool
def plus(n1,n2):
    print("Plus tool fire ----->")
    return f"your answer is {n1+n2}"

@function_tool
def subtract(n1,n2):
    print("Subtract tool fire ----->")
    return f"your answer is {n1-n2}"