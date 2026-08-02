from tavily import TavilyClient
from app.core.config import settings


class TavilySearchService:
    def __init__(self):
        print("Loaded Tavily Key:", settings.TAVILY_API_KEY)

        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    def search(self, topic: str):

        response = self.client.search(
            query=topic,
            search_depth="advanced",
            max_results=5
        )

        return response.get("results", [])