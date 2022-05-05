from pprint import pprint
import requests
import json

endpint1 = 'https://httpbin.org/anything'
endpint2 = 'http://localhost:8000/'
endpint3 = 'http://localhost:8000/random-product'
endpint4 = 'http://localhost:8000/add-product/'

# get_res = requests.get(endpint2, json={'name': 'Abdullah', 'age': 26}, params={'city': 'Jeddah'})
# get_res = requests.get(endpint3, json={'name': 'Abdullah', 'age': 26}, params={'city': 'Jeddah'})
get_res = requests.get(endpint3)
# get_res = requests.post(endpint4)

print(get_res.status_code)
data = json.loads(get_res.text)
print(data)