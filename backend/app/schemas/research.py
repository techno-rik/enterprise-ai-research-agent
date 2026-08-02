from typing import Any

from pydantic import BaseModel


class ResearchRequest(BaseModel):
    topic: str


class ResearchResponse(BaseModel):
    id: int
    topic: str
    status: str
    sources_found: int
    summary: Any