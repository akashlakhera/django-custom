from rest_framework import serializers
from quickstart.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ('name', 'price')
