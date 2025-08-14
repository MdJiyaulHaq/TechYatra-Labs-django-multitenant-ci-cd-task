from django.shortcuts import render  # noqa
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from django_tenants.utils import get_public_schema_name

from .models import Client
from .serializers import TenantSerializer


class TenantsList(APIView):
    def get(self, request, *args, **kwargs):
        public_schema = get_public_schema_name()
        current_schema = connection.schema_name
        if current_schema != public_schema:
            return Response(status=404)
        tenants = Client.objects.order_by("schema_name")
        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)
