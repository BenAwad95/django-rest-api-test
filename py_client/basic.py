import requests

endpint = 'https://httpbin.org/anything'

get_res = requests.get(endpint, json={'name': 'Abdullah', 'age': 26})

# print(get_res.text)
# print(get_res.json)

