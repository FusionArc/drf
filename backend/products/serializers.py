from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class META:
        model = Product,
        fields = [
            title,
            content,
            price
        ]