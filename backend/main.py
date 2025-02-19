from fastapi import FastAPI
from backend.ingestion import router as ingestion_router
from backend.retrieval import router as retrieval_router

app = FastAPI(
    title="Retrieval-Augmented Generation (RAG) API",
    description="A FastAPI-based RAG system using Weaviate for document storage and retrieval.",
    version="1.0.0"
)

# Include routers
app.include_router(ingestion_router, prefix="/api")
app.include_router(retrieval_router, prefix="/api")

@app.get("/", tags=["Health Check"])
def home():
    return {"message": "Welcome to the RAG System with Weaviate!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
