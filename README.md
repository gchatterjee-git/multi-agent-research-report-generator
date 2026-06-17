# Multi-Agent Research & Report Generator

A multi-agent system that autonomously researches topics and generates structured reports using Claude AI and CrewAI.

## Overview

Four specialised agents collaborate in sequence to produce a grounded, well-structured research report:

1. **Researcher** — gathers raw findings from the knowledge base and web
2. **Analyst** — synthesises findings into themes and implications
3. **Devil's Advocate** — challenges assumptions and surfaces gaps
4. **Writer** — integrates all outputs into a final Markdown report

## Project Structure

```
multi-agent-research-report-generator/
├── agents/
│   ├── researcher.py       # Gathers raw research from KB and web
│   ├── analyst.py          # Synthesises findings into insights
│   ├── devils_advocate.py  # Critiques assumptions and logic
│   ├── writer.py           # Produces the final Markdown report
│   └── test_agent.py       # Agent testing script
├── crew/
│   ├── crew.py             # Assembles and runs the full CrewAI pipeline
│   └── tasks.py            # Task definitions wired to each agent
├── retrieval/
│   ├── retriever.py        # LangChain MMR retriever from vector store
│   └── rag_chain.py        # Full RAG chain (retriever → prompt → Claude → output)
├── tools/
│   ├── web_search.py       # Tavily web search LangChain tool
│   ├── vector_search.py    # Knowledge base search LangChain tool
│   └── tools_test.py       # Manual tool testing script
├── ingestion/
│   ├── loader.py           # Document loading (.pdf, .txt)
│   ├── splitter.py         # Text chunking with overlap
│   ├── embedder.py         # HuggingFace local embeddings
│   ├── store.py            # ChromaDB vector store (create + load)
│   └── test.py             # End-to-end ingestion test script
├── tests/                  # Unit and integration tests
├── data/                   # Input documents (e.g. PDFs)
├── chroma_store/           # Persisted vector store (auto-generated)
├── output_report.md        # Generated report output
├── config.py               # Centralised config and env vars
└── requirements.txt
```

## What's Built

### 1. Ingestion Pipeline

Handles loading, chunking, embedding, and storing documents for retrieval.

| Module | Description |
|---|---|
| `loader.py` | Loads `.pdf` and `.txt` files via LangChain document loaders |
| `splitter.py` | Splits documents into overlapping chunks using `RecursiveCharacterTextSplitter` |
| `embedder.py` | Generates embeddings using `all-MiniLM-L6-v2` (runs locally, no API key needed) |
| `store.py` | Embeds chunks and persists them to ChromaDB; supports creating and loading a store |

### 2. Retrieval & RAG Chain

| Module | Description |
|---|---|
| `retriever.py` | Wraps ChromaDB with an MMR retriever (`k=5`, `fetch_k=10`) for diversity-aware retrieval |
| `rag_chain.py` | LCEL chain: retriever → context formatter → prompt → Claude Haiku → string output |

### 3. Tools

LangChain `Tool` wrappers that agents use to gather information.

| Tool | Description |
|---|---|
| `web_search.py` | Searches the web via Tavily; returns formatted results with source URLs |
| `vector_search.py` | Queries the private knowledge base via the RAG chain; returns grounded answers |

### 4. Agents

Each agent is a CrewAI `Agent` with a defined role, goal, and backstory.

| Agent | Role | Tools |
|---|---|---|
| `researcher.py` | Senior Research Analyst | `web_search`, `vector_search` |
| `analyst.py` | Senior Research Analyst | None (works from researcher output) |
| `devils_advocate.py` | Critical Reviewer | None (works from prior outputs) |
| `writer.py` | Research Report Writer | None (integrates all prior outputs) |

### 5. Crew & Tasks

| Module | Description |
|---|---|
| `tasks.py` | Defines 4 tasks (research → analysis → critique → writing) with explicit context chaining |
| `crew.py` | Assembles the crew, runs sequential process, saves output to `output_report.md` |

### Configuration

`config.py` centralises all settings:

| Variable | Value |
|---|---|
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` |
| `CHUNK_SIZE` | `500` |
| `CHUNK_OVERLAP` | `50` |
| `CHROMA_PATH` | `./chroma_store` |
| `COLLECTION_NAME` | `research_doc_col` |

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
```

### Required API Keys (.env)

```
ANTHROPIC_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

## Running the Research Crew

```bash
python -m crew.crew
```

This runs a full research pipeline on the default topic and saves the report to `output_report.md`. To change the topic, update the `topic` variable in `crew/crew.py`.

## Other Scripts

```bash
# Test the ingestion pipeline
python -m ingestion.test

# Test individual tools
python -m tools.tools_test
```

## Requirements

- Python 3.11+
- Anthropic API key
- Tavily API key
