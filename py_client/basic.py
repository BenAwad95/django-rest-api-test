import requests

endpint1 = 'https://httpbin.org/anything'
endpint2 = 'http://localhost:8000/'

get_res = requests.get(endpint2, json={'name': 'Abdullah', 'age': 26})

print(get_res.text)
print(get_res.json)
print(get_res.status_code)

