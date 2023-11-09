import requests
import json

endpoint = "http://localhost:8000/api/products/update/2/"

data = {"title": "new title2", "content": "some brand new content for the product"}

response = requests.put(endpoint, json=data)


data = json.dumps(response.json(), indent=2)

print(data)
