import PyPDF2
from docx import Document
import json

def extract_text(file_path, file_type):
    text = ""
    if file_type == "pdf":
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + " "
    elif file_type == "docx":
        doc = Document(file_path)
        text = " ".join([para.text for para in doc.paragraphs])
    elif file_type == "json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            text = json.dumps(data)
    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    return text
