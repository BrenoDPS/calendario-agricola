from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CulturaViewSet, BandejaViewSet, PlantioViewSet, NotificacaoViewSet

cal_router = DefaultRouter()
cal_router.register(r'culturas', CulturaViewSet)
cal_router.register(r'bandejas', BandejaViewSet)
cal_router.register(r'plantios', PlantioViewSet)
cal_router.register(r'notificacoes', NotificacaoViewSet)

urlpatterns = [
    path('', include(cal_router.urls)),
]
