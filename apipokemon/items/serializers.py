from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'identifier', 'category_id', 'cost', 'fling_power', 'fling_effect_id']