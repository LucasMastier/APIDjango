from rest_framework import serializers
from .models import Move

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'identifier', 'generation_id', 'type_id', 'power', 'pp','accuracy','priority','target_id','damage_class_id','effect_id','effect_chance','contest_type_id','super_contest_effect_id']