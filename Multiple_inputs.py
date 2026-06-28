# Exercise for Graph II — add OR multiply a list of numbers

from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    values: List[int]
    operation: str
    result: str


def process_values(state: AgentState) -> AgentState:
    """Adds or multiplies the values depending on the operation."""

    if state["operation"] == "+":
        answer = sum(state["values"])
    elif state["operation"] == "*":
        answer = 1
        for number in state["values"]:
            answer *= number

    state["result"] = f"Hi {state['name']}, your answer is: {answer}"
    return state


graph = StateGraph(AgentState)

graph.add_node("processor", process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

answers = app.invoke({"name": "Jack Sparrow", "values": [1, 2, 3, 4], "operation": "*"})
print(answers["result"])
