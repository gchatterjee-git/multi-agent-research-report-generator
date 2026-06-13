from langchain.tools import Tool
from retrieval.rag_chain import build_rag_chain

rag_chain = build_rag_chain()

def search_knowledge_base(query: str) -> str:
    """
    Query the private knowledge base (ingested documents).
    """
    answer = rag_chain.invoke(query)
    return answer

vector_search_tool = Tool(
    name="knowledge_base_search",
    description="""
        Search the private knowledge base of ingested research documents. 
        Use this when the question is about content from documents that have already been uploaded, 
        such as research papers, reports, or any files added during ingestion. 
        Prefer this over web_search when the topic is covered in the knowledge base -  
        it returns grounded answers from your own curated sources, not the open web. 
        Do NOT use this for current events, recent news, or topics not present in the ingested documents - 
        use web_search instead. 
        Input: a specific question about the document content. 
        Output: a synthesized answer drawn from the most relevant document chunks.""",
    func=search_knowledge_base
)