from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from stock.serializers import ItemSerializer
from stock.serializers import EvaluationFactSerializer
from stock.serializers import ValueSerializer
from stock.serializers import CalendarSerializer
from stock.serializers import EventHistSerializer
from stock.serializers import TradeHistSerializer

from stock.models import Item
from stock.models import EvaluationFact
from stock.models import Value
from stock.models import Calendar
from stock.models import EventHist
from stock.models import TradeHist

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('cd', 'nm', 'f_yn')

class EvaluationFactViewSet(viewsets.ModelViewSet):

    queryset = EvaluationFact.objects.all()
    serializer_class = EvaluationFactSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('item_key', 'value_pkey', 'value_ckey')

class ValueViewSet(viewsets.ModelViewSet):

    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class CalendarViewSet(viewsets.ModelViewSet):

    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class EventHistViewSet(viewsets.ModelViewSet):

    queryset = EventHist.objects.all()
    serializer_class = EventHistSerializer

class TradeHistViewSet(viewsets.ModelViewSet):

    queryset = TradeHist.objects.all()
    serializer_class = TradeHistSerializer