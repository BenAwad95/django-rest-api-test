from posixpath import basename
from django.urls import URLPattern
from rest_framework import routers

from product.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register('products-abc', ProductViewSet, basename='products')

print(router.urls)
urlpatterns = router.urls