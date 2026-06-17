from langchain.tools import Tool
from crewai.tools import tool
from tavily import TavilyClient
from config import TAVILY_API_KEY

@tool("web_search")
def web_search_tool(query: str) -> str:
    """
    Search the web for current information on a topic.
    - Use this when the question requires up-to-date facts, recent events,
        news, statistics, or information that may have changed after your training cutoff.
    - Also use this when the topic is not covered in the ingested documents.
    - Do NOT use this for questions that can be answered from the provided documents —
        use the vector_search tool instead.
    - Input: a concise search query string.
    - Output: Text excerpt from relevant web pages with their source URLs.
    """
    client = TavilyClient(api_key=TAVILY_API_KEY)
    responses = client.search(query=query, max_results=3)
    results = responses.get("results", [])
    if not results:
        return "No results found."
    return "\n\n".join(
        f"Source: {result['url']}\n{result['content']}"
        for result in results
    )