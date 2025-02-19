from fastapi import APIRouter
from pydantic import BaseModel
import weaviate
from sentence_transformers import SentenceTransformer
from .config import WEAVIATE_URL, EMBEDDING_MODEL

router = APIRouter()
client = weaviate.Client(url=WEAVIATE_URL)
model = SentenceTransformer(EMBEDDING_MODEL)

class QueryRequest(BaseModel):
    query: str

@router.post("/query/")
async def query_document(request: QueryRequest):
    query_vector = model.encode(request.query).tolist()
    
    # Fix: Pass dictionary instead of list
    results = client.query.get("Document", ["text", "filename"]) \
                         .with_near_vector({"vector": query_vector}) \
                         .with_limit(3) \
                         .do()

    return {"query": request.query, "results": results["data"]["Get"]["Document"]}
