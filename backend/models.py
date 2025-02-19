import weaviate

def create_weaviate_schema(client):
    schema = {
        "classes": [
            {
                "class": "Document",
                "vectorizer": "none",
                "properties": [
                    {"name": "text", "dataType": ["text"]},
                    {"name": "filename", "dataType": ["string"]},
                ],
            }
        ]
    }
    
    client.schema.delete_all()
    client.schema.create(schema)
