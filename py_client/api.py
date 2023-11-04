import requests
import json

endpoint = "http://localhost:8000/api/1/"

response = requests.get(
    endpoint, json={"data": "some data"}, params={"search_query": "miclem"}
)

data = json.dumps(response.json(), indent=4)
print(data)
