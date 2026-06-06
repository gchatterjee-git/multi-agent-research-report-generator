import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
CHROMA_PATH = "./chroma_store"
CHUNK_SIZE = 500       
CHUNK_OVERLAP = 50    
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Free local model — no API key needed
CHUNKING_STRATEGY = "fixed"