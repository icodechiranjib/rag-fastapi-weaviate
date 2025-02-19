from fastapi import APIRouter, UploadFile, File
from sentence_transformers import SentenceTransformer
import weaviate
import tempfile
import os
from .utils import extract_text
from .config import WEAVIATE_URL, EMBEDDING_MODEL

router = APIRouter()
client = weaviate.Client(url=WEAVIATE_URL)
model = SentenceTransformer(EMBEDDING_MODEL)

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    file_type = file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = extract_text(tmp_path, file_type)
    os.remove(tmp_path)

    embedding = model.encode(text).tolist()

    response = client.data_object.create(
        class_name="Document",
        data_object={"text": text, "filename": file.filename},
        vector=embedding
    )

    return {"message": "Document uploaded", "weaviate_id": response}
