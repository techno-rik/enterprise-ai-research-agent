from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class ResearchSession(Base):
    __tablename__ = "research_sessions"

    id = Column(Integer, primary_key=True, index=True)

    topic = Column(String, nullable=False)

    status = Column(String, default="CREATED")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sources = relationship("Source", back_populates="research")
    documents = relationship("Document", back_populates="research")
    findings = relationship("Finding", back_populates="research")
    reports = relationship("Report", back_populates="research")

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)

    research_id = Column(
        Integer,
        ForeignKey("research_sessions.id")
    )

    title = Column(String)

    url = Column(String)

    publisher = Column(String)

    research = relationship(
        "ResearchSession",
        back_populates="sources"
    )

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    research_id = Column(
        Integer,
        ForeignKey("research_sessions.id")
    )

    content = Column(Text)

    research = relationship(
        "ResearchSession",
        back_populates="documents"
    )

class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True)

    research_id = Column(
        Integer,
        ForeignKey("research_sessions.id")
    )

    finding = Column(Text)

    confidence = Column(Float)

    research = relationship(
        "ResearchSession",
        back_populates="findings"
    )

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)

    research_id = Column(
        Integer,
        ForeignKey("research_sessions.id")
    )

    summary = Column(Text)

    research = relationship(
        "ResearchSession",
        back_populates="reports"
    )

