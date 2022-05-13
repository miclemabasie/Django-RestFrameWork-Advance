import requests
import pprint


product_id = input("Please Enter the ID of the product you wish to get: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print("Prodcut ID not valid")

if product_id is not None:
    endpoint = "https://httpbin.org/status/200/"
    endpoint = "https://httpbin.org/anything"
    endpoint = f"http://localhost:8000/api/products/{product_id}"

    content = requests.get(url=endpoint)
    print(content.json())


