import json, requests

# list of products
# ------
# endpoint = 'http://localhost:8000/products/'
# get_respose = requests.get(endpoint)
# print(get_respose.status_code)
# data = json.loads(get_respose.text)
# ------

# details of a product
# ------
# endpoint = 'http://localhost:8000/products/1'
# get_respose = requests.get(endpoint)
# print(get_respose.status_code)
# print(json.loads(get_respose.text))
# ------

# delete of product
# ------
# endpoint = 'http://localhost:8000/products/del/5'
# del_respose = requests.delete(endpoint)
# print(del_respose.status_code)
# print(del_respose.text)
# ------

# create of product
# ------
# endpoint = 'http://localhost:8000/products/create/'
# new_product_data ={
#     'title': 'Pencil',
#     'price': 2.99,
#     'content': 'Stay for long peried of time'
# }
# post_respose = requests.post(endpoint, json=new_product_data)
# print(post_respose.status_code)
# print(post_respose.text)
# # ------

# create of product
# ------
endpoint = 'http://localhost:8000/products/update/1'
new_product_data ={
    'title': 'UPDATE',
    'price': 'err',
    'content': 'THIS PRODUCT HAS BEEN UPDATED'
}
put_respose = requests.put(endpoint, json=new_product_data)
print(put_respose.status_code)
print(put_respose.text)
# ------