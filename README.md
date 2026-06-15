# Multi-Agent Research & Report Generator

A multi-agent system that autonomously researches topics and generates structured reports using Claude AI.

## Overview

This project demonstrates a multi-agent architecture where specialized agents collaborate to:
- Search and gather information from multiple sources
- Analyze and synthesize research findings
- Generate well-structured, cited reports

## Project Structure

```
multi-agent-research-report-generator/
├── ingestion/
│   ├── loader.py           # Document loading (.pdf, .txt)
│   ├── splitter.py         # Text chunking with overlap
│   ├── embedder.py         # HuggingFace local embeddings
│   ├── store.py            # ChromaDB vector store (create + load)
│   └── test.py             # End-to-end ingestion test script
├── retrieval/
│   ├── retriever.py        # LangChain MMR retriever from vector store
│   └── rag_chain.py        # Full RAG chain (retriever → prompt → Claude → output)
├── tools/
│   ├── web_search.py       # Tavily web search LangChain tool
│   ├── vector_search.py    # Knowledge base search LangChain tool
│   └── tools_test.py       # Manual tool testing script
├── agents/
│   └── researcher.py       # Researcher agent (in progress)
├── workflows/              # Agent orchestration workflows (coming soon)
├── tests/                  # Unit and integration tests
├── data/                   # Input documents (e.g. PDFs)
├── chroma_store/           # Persisted vector store (auto-generated)
├── config.py               # Centralised config and env vars
└── requirements.txt
```

## What's Built So Far

### 1. Ingestion Pipeline

Handles loading, chunking, embedding, and storing documents for retrieval.

| Module | Description |
|---|---|
| `loader.py` | Loads `.pdf` and `.txt` files via LangChain document loaders |
| `splitter.py` | Splits documents into overlapping chunks using `RecursiveCharacterTextSplitter` |
| `embedder.py` | Generates embeddings using `all-MiniLM-L6-v2` (runs locally, no API key needed) |
| `store.py` | Embeds chunks and persists them to ChromaDB; supports creating and loading a store |

### 2. Retrieval & RAG Chain

Retrieves relevant chunks from the vector store and generates grounded answers.

| Module | Description |
|---|---|
| `retriever.py` | Wraps ChromaDB with an MMR retriever (`k=5`, `fetch_k=10`) for diversity-aware retrieval |
| `rag_chain.py` | LCEL chain: retriever → context formatter → prompt → Claude Haiku → string output |

### 3. Tools

LangChain `Tool` wrappers that agents can call to gather information.

| Tool | Description |
|---|---|
| `web_search.py` | Searches the web via Tavily; returns formatted results with source URLs |
| `vector_search.py` | Queries the private knowledge base via the RAG chain; returns grounded answers |

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

## Running the Ingestion Test

Place a PDF in the `data/` directory, update the path in `ingestion/test.py`, then run:

```bash
python -m ingestion.test
```

## Running the Tools Test

```bash
python -m tools.tools_test
```

## Requirements

- Python 3.11+
- Anthropic API key
- Tavily API key (for web search)
