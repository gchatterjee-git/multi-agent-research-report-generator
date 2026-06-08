# ingestion/loader.py
from langchain_community.document_loaders import (PyPDFLoader, 
                                                  TextLoader, 
                                                  Docx2txtLoader,
                                                  CSVLoader,
                                                  UnstructuredMarkdownLoader,
                                                  UnstructuredPowerPointLoader,
)
from pathlib import Path

def load_document(file_path: str) -> list:
    """
    Load a document from the given path.
    Supports: .pdf, .txt
    Returns: list of LangChain Document objects
    """
    extension = Path(file_path).suffix
    if extension == ".pdf":
        loader = PyPDFLoader(file_path)
    elif extension == ".txt":
        loader = TextLoader(file_path)
    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)
    elif extension == ".csv":
        loader = CSVLoader(file_path)
    elif extension == ".md":
        loader = UnstructuredMarkdownLoader(file_path)
    elif extension == ".pptx":
        loader = UnstructuredPowerPointLoader(file_path)
    else:
        raise ValueError(f"Unknown extension: {extension}")
    return loader.load()
