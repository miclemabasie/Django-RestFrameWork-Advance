import requests
from getpass import getpass


username = input("Enter Username: ")

password = getpass()

credentials = {
    "username": username,
    "password": password,
}

auth_endpoint = "http://localhost:8000/api/obtain-token/"

auth_response = requests.post(auth_endpoint, json=credentials)

if "token" in auth_response.json().keys():
    print("user successfully authenticated!")
    print("Checking permissions....")

    # Construct Authorization headers based on the auth token
    headers = {
        "Authorization": f"Token {auth_response.json()['token']}",
    }
    product_list_endpoint = "http://localhost:8000/api/products/"

    product_list_response = requests.get(product_list_endpoint, headers=headers)

    print(product_list_response.json())
