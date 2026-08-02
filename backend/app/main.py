from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Research Agent",
    version="1.0.0",
    description="AI-powered Enterprise Research Platform"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Research Agent API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }