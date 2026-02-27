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


# USER QUERY

query = input("Ask your question: ")

# Convert query to embedding

query_embedding = model.encode(query).tolist()


# Hybrid Search

response = es.search(
    index=INDEX_NAME,
    knn={
        "field": "embedding",
        "query_vector": query_embedding,
        "k": 3,
        "num_candidates": 10,
        "boost": 0.5
    },
    query={
        "match": {
            "text": {
                "query": query,
                "boost": 0.5
            }
        }
    }
)

# BUILD CONTEXT

context = ""

for hit in response["hits"]["hits"]:
    context += hit["_source"]["text"] + "\n"

print("\n--- Retrieved Context ---\n")
print(context)

print("\n--- Final Answer ---\n")

if context:
    print(f"Based on the indexed knowledge:\n{context}")
else:
    print("No relevant information found.")