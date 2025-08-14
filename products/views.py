from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import connection
from django_tenants.utils import get_public_schema_name

from .models import Product
from .serializers import ProductSerializer


class ProductListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        if connection.schema_name == get_public_schema_name():
            return Product.objects.none()
        return Product.objects.all()

    def list(self, request, *args, **kwargs):
        if connection.schema_name == get_public_schema_name():
            return generics.Response(status=404)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if connection.schema_name == get_public_schema_name():
            return generics.Response(status=404)
        return super().create(request, *args, **kwargs)
