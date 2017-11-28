from rest_framework import serializers

from stock.models import Item
from stock.models import EvaluationFact
from stock.models import Value
from stock.models import Calendar
from stock.models import EventHist
from stock.models import TradeHist

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

class EventHistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventHist
        fields = ('__all__')

class TradeHistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TradeHist
        fields = ('__all__')
