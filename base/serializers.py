from rest_framework import serializers
from .models import Timeline, Item


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    end = serializers.DateTimeField(allow_null=True, required=False)

    class Meta:
        model = Item
        fields = '__all__'
