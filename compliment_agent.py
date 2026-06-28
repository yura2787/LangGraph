# personalized compliment agent

from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

class AgentState(TypedDict):
    name: str


def compliment_node(state: AgentState) -> AgentState:
    """
    Simple node that adds a compliment to the state
    """
    state["name"] = f"{state['name']}, you're doing an amazing job learning LangGraph!"
    return state

graph = StateGraph(
    AgentState,
)

graph.add_node('compliment', compliment_node)
graph.set_entry_point('compliment')
graph.set_finish_point('compliment')


app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

result = app.invoke({"name": 'Bob'})
print(result)
