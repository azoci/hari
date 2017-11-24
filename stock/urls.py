from django.conf.urls import url, include
from stock import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'item', views.ItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]