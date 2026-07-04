# 🕸️ LangGraph AI Agents

A hands-on collection of **AI agents built with [LangGraph](https://langchain-ai.github.io/langgraph/)**, progressing from basic state graphs to a production-style **RAG agent** over a PDF knowledge base.

This repository demonstrates practical experience with **agentic AI workflows**: state management, conditional routing, loops, tool calling, memory, and retrieval-augmented generation.

---

## 🧰 Tech Stack

- **Python 3.12**
- **LangGraph** — agent orchestration (state graphs, nodes, edges)
- **LangChain** — LLM & tooling abstractions
- **Groq** — fast LLM inference (`llama-3.3-70b`, `gpt-oss-120b`)
- **ChromaDB** — vector database for RAG
- **HuggingFace Embeddings** — local, free text embeddings (`all-MiniLM-L6-v2`)

---

## 📂 Projects

| File | Concept | Description |
|------|---------|-------------|
| [`compliment_agent.py`](compliment_agent.py) | **Basic graph** | Single-node graph that builds a personalized message from state. |
| [`Multiple_inputs.py`](Multiple_inputs.py) | **Multiple inputs + branching** | Adds or multiplies a list of numbers based on an operation. |
| [`sequant.py`](sequant.py) | **Sequential nodes** | Passes state through three chained nodes that each enrich the result. |
| [`Conditional_agent.py`](Conditional_agent.py) | **Conditional edges** | Two routers dynamically choose add/subtract paths at runtime. |
| [`looping.py`](looping.py) | **Loops** | Automatic "higher or lower" number-guessing game using a self-loop. |
| [`Agent_bot.py`](Agent_bot.py) | **LLM chatbot** | Minimal conversational agent powered by an LLM. |
| [`Memory_agent.py`](Memory_agent.py) | **Conversational memory** | Chatbot that remembers full history and logs the conversation to a file. |
| [`React.py`](React.py) | **ReAct + tools** | Agent that reasons and calls math tools in a think→act→think loop. |
| [`Drafter.py`](Drafter.py) | **Tool-driven agent** | Interactive document assistant that updates and saves `.txt` documents. |
| [`Rag_agent.py`](Rag_agent.py) | **RAG (Retrieval-Augmented Generation)** | Answers questions about a PDF using ChromaDB + embeddings, with source citations. |

---

## 🚀 Getting Started

### 1. Clone & create a virtual environment (Python 3.12)
```bash
git clone https://github.com/yura2787/LangGraph.git
cd LangGraph
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies
```bash
pip install langgraph langchain langchain-core langchain-community \
            langchain-groq langchain-huggingface langchain-chroma \
            langchain-text-splitters chromadb pypdf sentence-transformers \
            python-dotenv
```

### 3. Add your API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_key_here
```
> Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

### 4. Run any agent
```bash
python Rag_agent.py      # RAG over the PDF
python Drafter.py        # document assistant
python React.py          # ReAct tool-using agent
```

---

## ⭐ Highlighted: RAG Agent

`Rag_agent.py` is the most complete example. It:

1. Loads a PDF and splits it into overlapping chunks.
2. Embeds the chunks locally (HuggingFace) and stores them in **ChromaDB**.
3. Runs a **ReAct loop**: the LLM decides when to search the document, retrieves the most relevant chunks, and answers **grounded in the source** — with citations and `temperature=0` to minimize hallucination.

```
Question → LLM → (needs lookup?) → Retriever → ChromaDB → relevant chunks → LLM → Answer
```

---

## 📌 What This Demonstrates

- Designing **stateful agent graphs** (nodes, edges, conditional routing, loops)
- **Tool calling** and multi-step reasoning (ReAct pattern)
- **Conversational memory** and persistence
- **RAG pipelines**: chunking, embeddings, vector search, grounded answers
- Working with multiple LLM providers and swapping models cleanly

---

## 📫 Contact

Open to freelance work on **AI agents, chatbots, and RAG systems**.
Feel free to reach out via GitHub.
