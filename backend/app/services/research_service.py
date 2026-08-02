import json
from sqlalchemy.orm import Session
from app.ai.summarizer import ResearchSummarizer
from app.database.models import (
    ResearchSession,
    Source,
    Finding,
)

from app.research.search import TavilySearchService


def create_research_session(
    db: Session,
    topic: str,
):

    session = ResearchSession(
        topic=topic
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    tavily = TavilySearchService()

    results = tavily.search(topic)

    summarizer = ResearchSummarizer()

    summary = summarizer.summarize(
    topic,
    results
)

    for result in results:

        source = Source(
            research_id=session.id,
            title=result.get("title"),
            url=result.get("url"),
            publisher=result.get("url")
        )

        db.add(source)

    db.commit()

    

    finding = Finding(
    research_id=session.id,
    finding=json.dumps(summary, indent=2),
    confidence=0.95
)

    db.add(finding)

    db.commit()

    return {
    "id": session.id,
    "topic": session.topic,
    "status": "COMPLETED",
    "sources_found": len(results),
    "summary": summary
}