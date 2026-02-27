from elasticsearch import Elasticsearch

ELASTIC_ENDPOINT = "https://my-elasticsearch-project-ca16ca.es.asia-south1.gcp.elastic.cloud:443"
API_KEY = "ZVJUVGxad0JycnlScjdUS0hwblg6RlJucWhuaVRCejJGRUIzQzhla3pMQQ=="

es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=API_KEY
)

index_name = "chatbot-docs"

mapping = {
    "mappings": {
        "properties": {
            "text": {
                "type": "text"
            },
            "embedding": {
                "type": "dense_vector",
                "dims": 384,
                "index": True,
                "similarity": "cosine"
            }
        }
    }
}

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists.")