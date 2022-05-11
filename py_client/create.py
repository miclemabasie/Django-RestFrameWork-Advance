import requests
import pprint



endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

content = requests.post(url=endpoint, json=({'title': 'Cats shoes', 'price': '12345'}))
print(content.json())