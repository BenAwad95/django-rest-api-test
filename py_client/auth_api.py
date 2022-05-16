import json, requests
from getpass import getpass


# auth_endpoint = "http://localhost:8000/auth/"
# password = getpass()

# auth_res = requests.post(auth_endpoint, json={'username': 'abdl', 'password': password})

# print(auth_res.json())
auth_res = {'status_code': 200}
if auth_res['status_code'] == 200:
    # token = auth_res.json()['token']
    token = "63d6a4517f602ead2120229764b92e3eea9e0b32"
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = 'http://localhost:8000/products/create/'
    new_product_data ={
        'title': 'Token 2',
        'price': 1455.7,
        'content': 'Learn and learn until you die'
    }
    post_respose = requests.post(endpoint, json=new_product_data, headers=headers)
    print(post_respose.status_code)
    print(post_respose.text)