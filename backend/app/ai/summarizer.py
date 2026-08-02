import json
from groq import Groq
from app.core.config import settings


class ResearchSummarizer:

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def summarize(self, topic: str, sources: list):

        context = ""

        for index, source in enumerate(sources, start=1):

            context += f"""
Source {index}

Title:
{source.get("title")}

Content:
{source.get("content", "")}

URL:
{source.get("url")}

-----------------------------------------
"""

        prompt = f"""
You are a Senior Enterprise AI Research Analyst.

Research Topic:
{topic}

Using ONLY the provided sources, generate a JSON response with EXACTLY this format.

{{
    "executive_summary":"...",
    "key_findings":[
        "...",
        "...",
        "..."
    ],
    "risks":[
        "...",
        "..."
    ],
    "opportunities":[
        "...",
        "..."
    ]
}}

Do NOT return markdown.

Return ONLY valid JSON.

Sources:

{context}
"""

        response = self.client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2,
    response_format={"type": "json_object"}
)

        return json.loads(response.choices[0].message.content)
