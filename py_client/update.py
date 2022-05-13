from itertools import product
import requests
import pprint

product_id = input("Enter the product ID: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print('Invalid product id')

if product_id is not None:


    endpoint = "https://httpbin.org/status/200/"
    endpoint = "https://httpbin.org/anything"
    endpoint = f"http://localhost:8000/api/products/{product_id}/update"

    data = {
        'title': 'This is my updated title',
        'price': 454.44
    }

    content = requests.put(url=endpoint, json=data)
    print(content.json())