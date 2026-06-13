from ingestion.store import load_vector_store

def get_retriever(k: int = 5):
    """
    Return a LangChain retriever from the vector store.
    
    What does k control? What happens if k is too high?
    What is MMR (Maximal Marginal Relevance) and when would you use it
    instead of plain similarity search?
    
    Attempt first, then ask Copilot: "What retriever search types does 
    LangChain's Chroma vectorstore support and when should I use each?"
    """
    store = load_vector_store()
    return store.as_retriever(
        search_type = "mmr",
        search_kwargs = {
            "fetch_k":10,
            "k":k,
            "lambda_mult":0.5
        }
    )