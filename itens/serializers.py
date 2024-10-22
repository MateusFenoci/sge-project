from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    size = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['id', 'product', 'size', 'quantity']
