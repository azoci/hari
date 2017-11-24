from rest_framework import serializers
from stock.models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('cd', 'nm', 'bizcd', 'biznm')