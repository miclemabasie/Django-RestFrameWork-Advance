import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Product Title",
    "content": "Product Content",
    "price": 5.3,
}

response = requests.post(endpoint, json=data)


print(response.json())
