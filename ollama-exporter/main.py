from fastapi import FastAPI

app = FastAPI(
    title="OLLAMA EXPORTER",
    description="OLLAMA EXPORTER REST API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.get("/")
async def root():
    """
    root endpoint
    """
    return {
        "service": "OLLAMA EXPORTER REST API",
        "version": "1.0.0",
        "status": "running",
        "description": "OLLAMA EXPORTER REST API",
        "endpoints": [
            "GET /"
        ]
    }