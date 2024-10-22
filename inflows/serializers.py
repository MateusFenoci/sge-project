# inflows/serializers.py

from rest_framework import serializers
from .models import Inflow


class InflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflow
        fields = ['id', 'supplier', 'item', 'quantity', 'description', 'created_at', 'updated_at']
