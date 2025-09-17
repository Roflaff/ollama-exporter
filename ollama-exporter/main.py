from fastapi import FastAPI

app = FastAPI(
    title="APM Service",
    description="A service for Application Performance Monitoring",
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
        "service": "APM Service REST API",
        "version": "1.0.0",
        "status": "running",
        "description": "A service for Application Performance Monitoring",
        "endpoints": [
            "GET /"
        ]
    }