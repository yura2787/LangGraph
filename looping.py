# Exercise for Graph V — Automatic Higher or Lower Game (looping)

import random
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    player_name: str
    guesses: List[int]
    attempts: int
    lower_bound: int
    upper_bound: int
    target_number: int
    hint: str


def setup_node(state: AgentState) -> AgentState:
    """Greets the player and picks the secret number to guess."""
    state["target_number"] = random.randint(state["lower_bound"], state["upper_bound"])
    state["hint"] = "start"
    print(f"Hi {state['player_name']}! I picked a secret number "
          f"between {state['lower_bound']} and {state['upper_bound']}.")
    return state


def guess_node(state: AgentState) -> AgentState:
    """Makes a smart guess in the middle of the current bounds."""
    guess = (state["lower_bound"] + state["upper_bound"]) // 2
    state["guesses"].append(guess)
    state["attempts"] += 1
    print(f"Attempt {state['attempts']}: guessing {guess} "
          f"(range {state['lower_bound']}-{state['upper_bound']})")
    return state


def hint_node(state: AgentState) -> AgentState:
    """Says higher / lower / correct and narrows the bounds accordingly."""
    guess = state["guesses"][-1]
    target = state["target_number"]

    if guess == target:
        state["hint"] = "correct"
        print(f"Correct! The number was {target}.")
    elif guess < target:
        state["hint"] = "higher"
        state["lower_bound"] = guess + 1   # the answer is above the guess
        print("Hint: higher")
    else:
        state["hint"] = "lower"
        state["upper_bound"] = guess - 1   # the answer is below the guess
        print("Hint: lower")

    return state


def should_continue(state: AgentState) -> str:
    """Decides whether to keep guessing or stop."""
    if state["hint"] == "correct":
        return "exit"          # we found it
    elif state["attempts"] >= 7:
        print("Out of attempts!")
        return "exit"          # used all 7 guesses
    else:
        return "loop"          # guess again


graph = StateGraph(AgentState)

graph.add_node("setup", setup_node)
graph.add_node("guess", guess_node)
graph.add_node("hint", hint_node)

graph.add_edge(START, "setup")
graph.add_edge("setup", "guess")
graph.add_edge("guess", "hint")

graph.add_conditional_edges(
    "hint",          # source node
    should_continue, # decision function
    {
        "loop": "guess",  # guess again
        "exit": END,      # stop the game
    },
)

app = graph.compile()

png_data = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_data)

result = app.invoke({
    "player_name": "Student",
    "guesses": [],
    "attempts": 0,
    "lower_bound": 1,
    "upper_bound": 20,
})

print("---")
print("Guesses made:", result["guesses"])
print("Secret number:", result["target_number"])
