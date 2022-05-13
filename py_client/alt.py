import requests
import pprint



endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/alt/5464564"

data = {
    'title': 'This is my new title',
    'content': 'This is my new content',
    'price': 15.99
}

content = requests.get(url=endpoint, json=data)
print(content.json())