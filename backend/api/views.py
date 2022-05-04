import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse
import pprint
from product.models import Product
# to convert model ins into dict
from django.forms.models import model_to_dict


def api_home(request):
    # request body data
    body = request.body # that give a json data type
    # print(body)
    # print(type(body))
    # convert to by string to json
    body_data = {}
    try: # I will use exception just in case the body is an empty
        body_data = json.loads(body)
    except JSONDecodeError:
        pass
    # add more data to body data
    body_data['headers'] = dict(request.headers)
    body_data['content_type'] = request.content_type
    # print(body_data)
    # url query params 
    # print(request.GET)
    # add url params into body data
    body_data['params'] = dict(request.GET)
    pprint.pprint(body_data, sort_dicts=False)

    # return JsonResponse({'massage':'Hello and welcome to our API django app'})
    return JsonResponse(body_data)

def get_random_product(request):
    ran_product = Product.objects.all().order_by('?').first()
    data = {}
    if ran_product:
        data = model_to_dict(ran_product)
    return JsonResponse(data)