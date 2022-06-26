from django.shortcuts import render

# views.py
from rest_framework import viewsets

from .serializers import ShopUnitSerializer
from .models import ShopUnit

class ShopUnitViewSet(viewsets.ModelViewSet):
    queryset = ShopUnit.objects.all().order_by('name')
    serializer_class = ShopUnitSerializer