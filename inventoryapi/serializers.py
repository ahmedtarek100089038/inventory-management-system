from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        
        fields = ('id', 'name')
        
class InventorySerializer(serializers.ModelSerializer):   
    
    # Show Supplier name
    supplier = serializers.StringRelatedField(many=True, read_only=True, required=False) 
    
    class Meta:
        model = Inventory
        
        fields = ('id', 'name', 'description', 'note', 'stock', 'availability', 'supplier')