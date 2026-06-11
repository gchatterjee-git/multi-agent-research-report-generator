# retrieval/rag_chain.py
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from retrieval.retriever import get_retriever

# Step 1: Write the prompt template yourself.
# What should it tell the LLM? What placeholders do you need?
RAG_PROMPT = ChatPromptTemplate.from_template("""
    You are a helpful assistant. Answer the question using only the context below.
    If the answer is not in the context, say "I don't have enough information to answer this."

    Context: 
    {context}

    Question:
    {question}

    Answer:  
""")

def format_docs(docs):
    """Join retrieved chunks into a single context string."""
    return "\n\n".join(doc.page_content for doc in docs)

def build_rag_chain():
    """
    Build and return the full RAG chain using LangChain's pipe (|) syntax.
    
    LCEL (LangChain Expression Language) uses | to chain steps.
    Attempt to build:
    retriever | format_docs → context
    question → passthrough
    both → prompt → llm → output_parser
    
    This will be confusing. That's fine. Try, fail, ask Copilot Chat:
    "Explain how LCEL RunnablePassthrough works in a RAG chain with an example"
    """
    retriever = get_retriever()
    llm = ChatAnthropic(model="claude-3-5-haiku-20241022", temperature=0)
    
    chain = (
        ...  # attempt this yourself first
    )
    return chain