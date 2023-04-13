from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ('id', 'name', 'created_DateTime')
        fields = '__all__'