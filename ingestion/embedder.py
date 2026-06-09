from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL
from functools import lru_cache

@lru_cache(maxsize=1)
def get_embeddings_model():
    """
    Return a HuggingFaceEmbeddings instance using a local sentence-transformers model.
    No API key required — the model runs on your machine.
    """
    return HuggingFaceEmbeddings(model_name = EMBEDDING_MODEL)