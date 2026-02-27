from elasticsearch import Elasticsearch

ELASTIC_ENDPOINT = "https://my-elasticsearch-project-ca16ca.es.asia-south1.gcp.elastic.cloud:443"
API_KEY = "write your elastic api key here"

es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=API_KEY
)

response = es.info()
print(response)
