from groq import Groq

from app.core.config import settings
from app.vectorstore.chroma import ChromaVectorStore


class ChatService:

    def __init__(self):
        self.vector_db = ChromaVectorStore()

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def ask(self, question: str):

        results = self.vector_db.search(
            question,
            k=5
        )

        documents = results.get("documents", [])

        if not documents or not documents[0]:
            return {
                "answer": "I couldn't find any relevant research in the knowledge base. Please run a research query first.",
                "sources_used": 0
            }

        documents = documents[0]

        context = "\n\n".join(
            doc[:1200] for doc in documents
        )

        print("\n========== CONTEXT SENT TO GROQ ==========\n")
        print(context)
        print("\n==========================================\n")

        prompt = f"""
You are an Enterprise AI Research Assistant.

Answer the user's question ONLY using the context below.

If the answer is not contained in the context, say:
"I don't have enough information."

Context:

{context}

Question:

{question}
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return {
            "answer": response.choices[0].message.content,
            "sources_used": len(documents)
        }