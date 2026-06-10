# notebook: 03_vector_store.ipynb

# 1. Ingest a document
from ingestion.loader import load_document
from ingestion.splitter import split_documents
from ingestion.store import create_vector_store
import shutil
import os
from config import CHROMA_PATH

# Add this at the top of your notebook before create_vector_store()
if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)
    print("Cleared existing store")


docs = load_document("/Users/gaurav/ai-engineering-from-scratch/projects/multi-agent-research-report-generator/data/Retrieval-augmented_generation.pdf")
chunks = split_documents(docs, chunk_size=500, chunk_overlap=50)
store = create_vector_store(chunks)

results = store.similarity_search("What problems does RAG solve in language models?", k=3)
for i, r in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(r.page_content)
    print(f"Source metadata: {r.metadata}")
    

# 3. Now try similarity_search_with_score — look at the distance numbers
results_scored = store.similarity_search_with_score("What problems does RAG solve in language models?", k=3)
for doc, score in results_scored:
    print(f"Score: {score:.4f} | {doc.page_content[:500]}")