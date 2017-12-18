from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.db import connection

from stock.serializers import ItemSerializer
from stock.serializers import EvaluationFactSerializer
from stock.serializers import ValueSerializer
from stock.serializers import CalendarSerializer
from stock.serializers import EventHistSerializer
from stock.serializers import TradeHistSerializer
from stock.serializers import ItemInvestSerializer
from stock.serializers import EvaluationFactInvestSerializer


from stock.models import Item
from stock.models import EvaluationFact
from stock.models import Value
from stock.models import Calendar
from stock.models import EventHist
from stock.models import TradeHist
from django.db.models import F, DecimalField, Sum, When, Case

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


    queryset = TradeHist.objects.annotate(nm=F('item_key__nm'))
    serializer_class = TradeHistSerializer

class ItemInvestViewSet(viewsets.ModelViewSet):

    #queryset = Item.objects.filter(tradehist__num__gt=0).annotate(
    queryset = Item.objects.filter(f_yn='Y').annotate(
        buy_amt=(Sum(
            Case(When(tradehist__type_nm='매수', then='tradehist__num'),
                default=0,
                output_field=DecimalField()
            )
        ) - Sum(
            Case(When(tradehist__type_nm='매도', then='tradehist__num'),
                default=0,
                output_field=DecimalField()
            )
        )) * Sum(
            Case(When(tradehist__type_nm='매수', then='tradehist__amt'),
                default=0,
                output_field=DecimalField()
            )
        ) / Sum(
            Case(When(tradehist__type_nm='매수', then='tradehist__num'),
                default=0,
                output_field=DecimalField()
            )
        ),
        buy_price=Sum(
            Case(When(tradehist__type_nm='매수', then='tradehist__amt'),
                default=0,
                output_field=DecimalField()
            )
        ) / Sum(
            Case(When(tradehist__type_nm='매수', then='tradehist__num'),
                default=0,
                output_field=DecimalField()
            )
        )
    ).order_by('skey')
    serializer_class = ItemInvestSerializer

class EvaluationFactInvestViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.filter(f_yn='Y').filter(evaluationfact__value_ckey__in=['403', '404', '405']).annotate(
        value_pkey=F('evaluationfact__value_pkey'),
        value_ckey=F('evaluationfact__value_ckey'),
        tvalue=F('evaluationfact__tvalue'),
        pvalue=F('evaluationfact__pvalue'),
        ppvalue=F('evaluationfact__ppvalue')
    ).order_by('skey', 'evaluationfact__value_ckey')
    serializer_class = EvaluationFactInvestSerializer
