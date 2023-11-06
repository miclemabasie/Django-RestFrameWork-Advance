import requests
import json

# endpoint = "http://localhost:8000/api/1/"
endpoint = "http://localhost:8000/api/post/"

response = requests.post(
    endpoint,
    json={"title": "New Product", "content": "some data"},
    params={"search_query": "miclem"},
)

data = json.dumps(response.json(), indent=4)
print(data)
