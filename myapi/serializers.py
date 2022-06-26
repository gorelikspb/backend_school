from rest_framework import serializers

from .models import ShopUnit

class ShopUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopUnit
        fields = ('id', 'name', 'date', 'type', 'price')        


