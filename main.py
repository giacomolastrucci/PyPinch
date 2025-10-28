from src.schemas import StreamData, Options
from src.PyPinch import PyPinch

streams_data = [
    StreamData(CP=20, TSUPPLY=180, TTARGET=80),
    StreamData(CP=40, TSUPPLY=130, TTARGET=40),
    StreamData(CP=80, TSUPPLY=60, TTARGET=100),
    StreamData(CP=36, TSUPPLY=30, TTARGET=120)
]

def pinch_tool(streams_data: list[StreamData], deltaT_min: float):

    pinch = PyPinch(streams_data, deltaT_min=deltaT_min)
    result = pinch.solve({Options.RETURN_RESULTS.value})
    return result

def main():
    result = pinch_tool(streams_data, deltaT_min=10)
    print(result)

if __name__ == "__main__":
    main()
