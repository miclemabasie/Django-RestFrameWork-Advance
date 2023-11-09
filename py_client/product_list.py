import requests

endpoint = (
    "http://localhost:8000/api/products/"  # incoporated list view with createview
)
# endpoint = "http://localhost:8000/api/products/list/" # independent list view


response = requests.get(endpoint)

print(response.json())
