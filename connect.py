from elasticsearch import Elasticsearch

ELASTIC_ENDPOINT = "https://my-elasticsearch-project-ca16ca.es.asia-south1.gcp.elastic.cloud:443"
API_KEY = "ZVJUVGxad0JycnlScjdUS0hwblg6RlJucWhuaVRCejJGRUIzQzhla3pMQQ=="

es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=API_KEY
)

response = es.info()
print(response)