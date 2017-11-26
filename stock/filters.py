from django_filters import rest_framework as filters
from stock import Item

class ItemFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('cd', 'nm', 'f_yn')