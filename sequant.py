# Exercise for Graph III — sequence of three nodes (name, age, skills)

from typing import TypedDict, List
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name: str
    age: int
    skills: List[str]
    result: str


def first_node(state: AgentState) -> AgentState:
    """Personalizes the name with a greeting."""
    state["result"] = f"{state['name']}, welcome to the system!"
    return state


def second_node(state: AgentState) -> AgentState:
    """Describes the user's age."""
    state["result"] = state["result"] + f" You are {state['age']} years old!"
    return state


def third_node(state: AgentState) -> AgentState:
    """Lists the user's skills in a formatted string."""
    skills = ", ".join(state["skills"][:-1]) + ", and " + state["skills"][-1]
    state["result"] = state["result"] + f" You have skills in: {skills}"
    return state


graph = StateGraph(AgentState)

graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")

app = graph.compile()



result = app.invoke({
    "name": "Linda",
    "age": 31,
    "skills": ["Python", "Machine Learning", "LangGraph"],
})
print(result["result"])
