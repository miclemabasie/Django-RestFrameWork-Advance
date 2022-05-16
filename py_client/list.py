import requests
import pprint
from getpass import getpass


username = input('Please Enter a username: \n')

user_password = getpass("Enter your password: \n")


get_token_endpoint = "http://localhost:8000/api/auth/"
get_auth_token = requests.post(get_token_endpoint, json={'username': username, 'password': user_password})

if 'token' in get_auth_token.json():
    token_ = get_auth_token.json()['token']
    print(get_auth_token.json())
    headers = {
        'Authorization': f"Bearer {token_}"
    }


    endpoint = "http://localhost:8000/api/products/"

    content = requests.get(endpoint, headers=headers)

    pprint.pprint(content.json())

else:
    print('No token can be created for this user.')

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
