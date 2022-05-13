import requests
import pprint


product_id = input('Enter the ID of product you wish to delete: ')
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id}: is not a valid product ID")

if product_id:
    endpoint = "https://httpbin.org/status/200/"
    endpoint = "https://httpbin.org/anything"
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

 
    content = requests.delete(url=endpoint)
    print(content.status_code, content.status_code == 204)