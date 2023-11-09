import json

import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

# endpoint = "http://localhost:8000"
response = ""

response = requests.get(endpoint, json={"name": "miclem abasie"})  # json data
# response = requests.get(endpoint, data={"name": "miclem abasie"}) # form data

# response = requests.get(endpoint)

data = json.dumps(response.json(), indent=2)

print(data)
