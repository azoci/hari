from django.conf.urls import url, include
from stock import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'value', views.ValueViewSet)
router.register(r'calendar', views.CalendarViewSet)
router.register(r'analysis', views.EvaluationFactViewSet)
router.register(r'noticefact', views.NoticeFactViewSet)
router.register(r'event', views.EventHistViewSet)
router.register(r'trade', views.TradeHistViewSet)
router.register(r'personal/item', views.ItemInvestViewSet)
router.register(r'personal/analysis', views.EvaluationFactInvestViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token)
]