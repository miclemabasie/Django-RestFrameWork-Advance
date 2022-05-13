import requests
import pprint



endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

content = requests.get(url=endpoint)
pprint.pprint(content.json())