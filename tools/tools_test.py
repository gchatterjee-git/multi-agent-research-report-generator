from tools.web_search import search_web
from tools.vector_search import search_knowledge_base

# Web search
result = search_web("Latest research on LLM fine-tuning")
print(result)
print(type(result))  # Must be str

# Vector search
result = search_knowledge_base("What is the language model chunking strategy?")
print(result)
