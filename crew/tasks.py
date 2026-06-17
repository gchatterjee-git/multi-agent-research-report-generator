# crew/tasks.py
from crewai import Task

def create_tasks(topic: str, researcher, analyst, devil, writer) -> list[Task]:

    research_task = Task(
        description=(
            f"Research the following topic comprehensively: {topic}\n\n"
            "Use both the knowledge base and web search tools. "
            "Prioritise primary sources — papers, official reports, expert writing. "
            "Do NOT interpret or synthesise — return raw findings only. "
            "Minimum 5 distinct findings from at least 3 different sources."
        ),
        expected_output=(
            "A structured document containing:\n"
            "1. 5-7 key findings as bullet points, each one sentence\n"
            "2. Each finding followed by its source URL in parentheses\n"
            "3. A 'Conflicting Evidence' section if sources disagree\n"
            "4. A 'Gaps' section listing what could not be found"
        ),
        agent=researcher
    )

    analysis_task = Task(
        description=(
            "Analyse the research findings provided by the researcher.\n\n"
            "Do NOT summarise — synthesise. Identify patterns across findings, "
            "logical implications, and what the evidence means for practitioners. "
            "Do NOT search for new information. Work only with what the researcher provided."
        ),
        expected_output=(
            "A structured analysis containing:\n"
            "1. 3-5 key themes or patterns identified across the findings\n"
            "2. Implications — what do these findings mean in practice?\n"
            "3. Surprising or counterintuitive observations\n"
            "4. Open questions the research raises but does not answer"
        ),
        agent=analyst,
        context=[research_task]
    )

    critique_task = Task(
        description=(
            "Review the research and analysis critically.\n\n"
            "Your job is to strengthen the final report by surfacing what is weak, "
            "missing, or assumed without evidence. Be specific — name the exact claim "
            "or finding you are challenging and explain why. "
            "Acknowledge what is well-supported before critiquing what is not."
        ),
        expected_output=(
            "A critique document containing:\n"
            "1. 2-3 well-supported claims worth keeping as-is\n"
            "2. 3-5 specific weaknesses — each naming the claim and the problem with it\n"
            "3. Alternative interpretations the analyst may have missed\n"
            "4. Risks or limitations not addressed in the research or analysis"
        ),
        agent=devil,
        context=[research_task, analysis_task]
    )

    writing_task = Task(
        description=(
            f"Write a comprehensive research report on: {topic}\n\n"
            "Integrate the researcher's findings, analyst's synthesis, and critic's "
            "challenges into a coherent narrative. Every claim must be traceable to "
            "the research or analysis. Format in clean Markdown."
        ),
        expected_output=(
            "A complete Markdown report with the following sections:\n"
            "# [Topic Title]\n"
            "## Executive Summary (3-4 sentences)\n"
            "## Key Findings (from researcher, with citations)\n"
            "## Analysis & Implications (from analyst)\n"
            "## Critical Perspective & Limitations (from devil's advocate)\n"
            "## Conclusion (2-3 sentences)\n"
            "## Sources (all URLs referenced)"
        ),
        agent=writer,
        context=[research_task, analysis_task, critique_task]
    )

    return [research_task, analysis_task, critique_task, writing_task]