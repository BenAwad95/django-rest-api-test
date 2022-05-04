from django.urls import path
from .views import api_home, get_random_product, add_product

urlpatterns = [
    path('', api_home, name='api_home'),
    path('random-product/', get_random_product, name='ran_product'),
    path('add-product/', add_product, name='add_product')
]
