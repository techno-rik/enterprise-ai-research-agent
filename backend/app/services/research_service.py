from sqlalchemy.orm import Session

from app.database.models import (
    ResearchSession,
    Source,
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

    for result in results:

        source = Source(
            research_id=session.id,
            title=result.get("title"),
            url=result.get("url"),
            publisher=result.get("url")
        )

        db.add(source)

    db.commit()

    return session