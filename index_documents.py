from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


# CONFIG

ELASTIC_ENDPOINT = "https://my-elasticsearch-project-ca16ca.es.asia-south1.gcp.elastic.cloud:443"
API_KEY = "ZVJUVGxad0JycnlScjdUS0hwblg6RlJucWhuaVRCejJGRUIzQzhla3pMQQ=="
INDEX_NAME = "chatbot-docs"


# CONNECT TO ELASTIC

es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=API_KEY
)


# LOAD EMBEDDING MODEL

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# SAMPLE DOCUMENTS

documents = [
    "Elasticsearch is a distributed search and analytics engine built on Apache Lucene.",
    "Vector search allows semantic similarity search using dense embeddings.",
    "Retrieval-Augmented Generation combines search with large language models.",
    "Hybrid search combines keyword and vector search for better relevance.",
    "Elasticsearch Serverless automatically scales without managing nodes."
]


# INDEX DOCUMENTS

for i, doc in enumerate(documents):
    embedding = model.encode(doc).tolist()

    es.index(
        index=INDEX_NAME,
        id=i,
        document={
            "text": doc,
            "embedding": embedding
        }
    )

print("Documents indexed successfully!")