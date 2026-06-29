# Exercise for Graph IV — two routers with conditional edges

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int

    number3: int
    number4: int
    operation2: str

    finalNumber: int
    finalNumber2: int


# ---- first pair of operation nodes (work on number1 & number2) ----

def adder(state: AgentState) -> AgentState:
    """This node adds the 2 numbers"""
    state["finalNumber"] = state["number1"] + state["number2"]
    return state


def subtractor(state: AgentState) -> AgentState:
    """This node subtracts the 2 numbers"""
    state["finalNumber"] = state["number1"] - state["number2"]
    return state


def decide_next_node(state: AgentState) -> str:
    """This node will select the next node of the graph"""
    if state["operation"] == "+":
        return "addition_operation"
    elif state["operation"] == "-":
        return "subtraction_operation"


# ---- second pair of operation nodes (work on number3 & number4) ----

def adder2(state: AgentState) -> AgentState:
    """This node adds the 2 numbers"""
    state["finalNumber2"] = state["number3"] + state["number4"]
    return state


def subtractor2(state: AgentState) -> AgentState:
    """This node subtracts the 2 numbers"""
    state["finalNumber2"] = state["number3"] - state["number4"]
    return state


def decide_next_node2(state: AgentState) -> str:
    """This node will select the next node of the graph"""
    if state["operation2"] == "+":
        return "addition_operation"
    elif state["operation2"] == "-":
        return "subtraction_operation"


graph = StateGraph(AgentState)

graph.add_node("add_node", adder)
graph.add_node("subtract_node", subtractor)
graph.add_node("router", lambda state: state)  # passthrough function

graph.add_node("add_node2", adder2)
graph.add_node("subtract_node2", subtractor2)
graph.add_node("router2", lambda state: state)  # passthrough function

graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        # Edge: Node
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node",
    },
)

# both first-stage nodes flow into the second router
graph.add_edge("add_node", "router2")
graph.add_edge("subtract_node", "router2")

graph.add_conditional_edges(
    "router2",
    decide_next_node2,
    {
        "addition_operation": "add_node2",
        "subtraction_operation": "subtract_node2",
    },
)

graph.add_edge("add_node2", END)
graph.add_edge("subtract_node2", END)

app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

initial_state = AgentState(
    number1=10, operation="-", number2=5,
    number3=7, number4=2, operation2="+",
    finalNumber=0, finalNumber2=0,
)

result = app.invoke(initial_state)
print(result)
print(f"finalNumber  (10 - 5) = {result['finalNumber']}")
print(f"finalNumber2 (7 + 2)  = {result['finalNumber2']}")
