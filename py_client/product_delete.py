import requests
import json


endpoint = "http://localhost:8000/api/products/delete/13/"

response = requests.delete(endpoint)

res_data = json.dumps(response.json(), indent=4)

print(res_data)
