import requests
import pprint



endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000"

content = requests.get(url=endpoint)
# pprint.pprint(content.json())
content=content.json()
pprint.pprint(content)

print(f"The use's name is: {content['name']}")

print(f"The user's age is: {content['age']} is_married: {content['is_male']}")


# HTTP Request => HTML
# REST API HTTP Request => JSON (xml, yaml)


