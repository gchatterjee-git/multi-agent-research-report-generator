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
├── agents/          # Individual agent definitions
├── tools/           # Shared tools (search, scrape, summarize)
├── workflows/       # Agent orchestration workflows
├── outputs/         # Generated reports
└── tests/           # Unit and integration tests
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
```

## Usage

```bash
python main.py --topic "Your research topic here"
```

## Requirements

- Python 3.11+
- Anthropic API key
