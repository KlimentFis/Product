from rest_framework import serializers
from main.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')
        extra_kwargs = {
            'id': {'read_only': True}  # id только для чтения
        }