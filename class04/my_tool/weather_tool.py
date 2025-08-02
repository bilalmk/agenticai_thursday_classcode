from agents import function_tool


@function_tool
def fetch_weather(city: str) -> str:
    """
        fetch the weather data
    """
    print("city>>>",city)
    return f"The weather in {city} is sunny"