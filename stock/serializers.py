from rest_framework import serializers

from stock.models import Item
from stock.models import EvaluationFact
from stock.models import Value
from stock.models import Calendar

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

class EvaluationFactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvaluationFact
        fields = ('__all__')

class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = ('__all__')

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ('__all__')
