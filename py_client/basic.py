import requests
import pprint



endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

content = requests.post(url=endpoint, params={"id": 2}, json={'title': 'hello world', "content": 'prodcut title', 'price': 'this'})
# pprint.pprint(content.json())
content=content.json()
pprint.pprint(content)


# HTTP Request => HTML
# REST API HTTP Request => JSON (xml, yaml)
