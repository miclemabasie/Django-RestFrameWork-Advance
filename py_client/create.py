import requests
import pprint
from getpass import getpass

username = input('Enter username: \n')
password = getpass('Enter Password: \n')

auth_endpoint = 'http://localhost:8000/api/auth/'

auth_resquest = requests.post(auth_endpoint, json={'username': username, 'password': password})
auth_response = auth_resquest.json()

if auth_resquest.status_code == 200:
    endpoint = "http://localhost:8000/api/products/"
    token_ = auth_response['token']
    headers = {
        "Authorization": f"Bearer {token_}"
    }

    data = {
        'title': 'Auth title',
        'content': 'Auth content',
        'price': 32.99
    }
    
    create_request = requests.post(endpoint, json=data, headers=headers)

    print(create_request.status_code)
    print(create_request.json())

