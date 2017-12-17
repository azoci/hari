from django.conf.urls import url, include
from stock import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'value', views.ValueViewSet)
router.register(r'calendar', views.CalendarViewSet)
router.register(r'analysis', views.EvaluationFactViewSet)
router.register(r'event', views.EventHistViewSet)
router.register(r'trade', views.TradeHistViewSet)
router.register(r'invest/item', views.ItemInvestViewSet)
router.register(r'invest/analysis', views.EvaluationFactInvestViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]