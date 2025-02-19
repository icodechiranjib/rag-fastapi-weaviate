import os

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
