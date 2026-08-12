import chromadb


class ChromaVectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            "research"
        )

    def add_documents(
        self,
        research_id: int,
        sources: list
    ):

        for index, source in enumerate(sources):

            content = (
                source.get("raw_content")
                or source.get("content")
                or ""
            )

            text = f"""
Title:
{source.get("title")}

Content:
{content}

URL:
{source.get("url")}
"""

            self.collection.add(
                ids=[
                    f"{research_id}_{index}"
                ],
                documents=[
                    text
                ],
                metadatas=[
                    {
                        "research_id": research_id,
                        "url": source.get("url")
                    }
                ]
            )

    def search(
        self,
        query: str,
        k: int = 5
    ):

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        return results