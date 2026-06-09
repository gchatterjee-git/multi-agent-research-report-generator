# ingestion/store.py
import chromadb
from langchain_chroma import Chroma
from ingestion.embedder import get_embeddings_model
from config import CHROMA_PATH, COLLECTION_NAME

def create_vector_store(chunks: list, collection_name: str = COLLECTION_NAME):
    """
    Embed chunks and store them in ChromaDB.
    Returns the vector store object.
    
    Attempt this yourself. Key question: does Chroma.from_documents()
    do the embedding for you, or do you pass pre-computed vectors?
    """
    embeddings = get_embeddings_model()
    store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=collection_name,
        collection_metadata={"hnsw_space":"cosine"}
    )
    return store

def load_vector_store(collection_name: str = COLLECTION_NAME):
    """
    Load an existing ChromaDB store from disk.
    When would you call this vs create_vector_store()?
    """
    embeddings = get_embeddings_model()
    store = Chroma(
        embedding_function=embeddings,
        collection_name=collection_name,
        persist_directory=CHROMA_PATH
    )
    return store
