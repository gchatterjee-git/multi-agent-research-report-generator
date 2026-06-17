from crewai import Agent, LLM
from langchain_anthropic import ChatAnthropic
from tools.web_search import web_search_tool
from tools.vector_search import search_knowledge_base
from crewai.tools import tool 

def create_researcher_agent(llm) -> Agent:
    agent = Agent(
        role="""
        Senior Research Analyst
        """,
        
        goal="""
            Gather comprehensive, well-cited information on a given topic by querying 
            the knowledge base and web. Return raw findings — facts, data, quotes, and 
            sources. Do NOT synthesise or interpret. Leave that to the analyst.""",
        
        backstory="""
        You are an investigative researcher with years of experience sourcing information 
        from academic papers, news, and databases. You are thorough and precise. 
        You cite every claim with its source URL and never present speculation as fact. 
        When sources conflict, you report both sides without picking one. 
        Your output is raw material — structured notes, not conclusions.
        """,
        
        tools=[web_search_tool, search_knowledge_base],
        llm=llm,
        verbose=True,          # Always True during development — watch it think
        allow_delegation=False  # Keep False for now, enable later as a stretch goal
        )
    return agent