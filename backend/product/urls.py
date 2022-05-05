from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='list_product'),
    path('create/', views.ProductCreateAPIView.as_view(), name='create_product'),
    path('<int:pk>', views.ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('update/<int:pk>', views.ProductUpdateAPIView.as_view(), name='update_product'),
    path('del/<int:pk>', views.ProductDestroyAPIView.as_view(), name='delete-product'),

]