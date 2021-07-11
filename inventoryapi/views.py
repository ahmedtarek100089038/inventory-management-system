# from django.shortcuts import render

from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.

# Serializer version, does all the CRUD
class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class InventoryView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer