# crew/crew.py
from crewai import Crew, Process, LLM
from agents.researcher import create_researcher_agent
from agents.analyst import create_analyst_agent
from agents.devils_advocate import create_devils_advocate_agent
from agents.writer import create_writer_agent
from crew.tasks import create_tasks

def run_research_crew(topic: str) -> str:
    """
    Assemble the crew and run a full research job.
    Returns the final written report as a string.
    """
    llm = LLM(model="anthropic/claude-haiku-4-5-20251001", temperature=0.1)

    researcher = create_researcher_agent(llm)
    analyst    = create_analyst_agent(llm)
    devil      = create_devils_advocate_agent(llm)
    writer     = create_writer_agent(llm)

    tasks = create_tasks(topic, researcher, analyst, devil, writer)

    crew = Crew(
        agents=[researcher, analyst, devil, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    topic = "The impact of open-source LLMs on enterprise AI adoption"
    report = run_research_crew(topic)

    with open("output_report.md", "w") as f:
        f.write(report)

    print("Report saved to output_report.md")