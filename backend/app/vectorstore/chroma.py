import chromadb

from sentence_transformers import SentenceTransformer


class ChromaVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            "research"
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
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

            embedding = self.model.encode(text).tolist()

            self.collection.add(
                ids=[
                    f"{research_id}_{index}"
                ],
                embeddings=[
                    embedding
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

        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results