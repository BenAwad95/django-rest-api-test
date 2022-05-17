from rest_framework import permissions, authentication
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from .models import Product
from .serializers import ProductSerializer
from .mixins import StaffEditorPermissionMixin


class ProductRetrieveAPIView(
    StaffEditorPermissionMixin,
    RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # WE DON'T NEED IT ANYMORE AFTER WE SET THE REST FRAMEWORK AT SETTINGS
    # authentication_classes = [authentication.SessionAuthentication]



class ProductListAPIView(
    StaffEditorPermissionMixin,
    ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # WE DON'T NEED IT ANYMORE AFTER WE SET THE REST FRAMEWORK AT SETTINGS
    # authentication_classes = [authentication.SessionAuthentication]




class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # WE DON'T NEED IT ANYMORE AFTER WE SET THE REST FRAMEWORK AT SETTINGS
    # authentication_classes = [authentication.SessionAuthentication]



class ProductCreateAPIView(
    StaffEditorPermissionMixin,
    CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # edit before save 
    # def perform_create(self, serializer):
        # some_filed = serializer.validated_data.get('title')
        # serializer.save(some_field = form_field)



class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # WE DON'T NEED IT ANYMORE AFTER WE SET THE REST FRAMEWORK AT SETTINGS
    # authentication_classes = [authentication.SessionAuthentication]

