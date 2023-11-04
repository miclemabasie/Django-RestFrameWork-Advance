import requests
import json

endpoint = "http://localhost:8000/products/api/"

response = requests.post(endpoint, json={"name": "miclem"})

data = json.dumps(response.json())

print(data)
