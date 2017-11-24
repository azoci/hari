from django.shortcuts import render
from rest_framework import viewsets
from stock.serializers import ItemSerializer
from stock.models import Item
# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
