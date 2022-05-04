from pprint import pprint
import requests
import json

endpint1 = 'https://httpbin.org/anything'
endpint2 = 'http://localhost:8000/'
endpint3 = 'http://localhost:8000/random-product'

# get_res = requests.get(endpint2, json={'name': 'Abdullah', 'age': 26}, params={'city': 'Jeddah'})
get_res = requests.get(endpint3, json={'name': 'Abdullah', 'age': 26}, params={'city': 'Jeddah'})

print(get_res.status_code)
data = json.loads(get_res.text)
print(data)
print(type(data['price']))