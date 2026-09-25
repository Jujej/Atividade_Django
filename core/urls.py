from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilamentoViewSet, Modelo3DViewSet

router = DefaultRouter()
router.register('filamentos', FilamentoViewSet, basename='filamento')
router.register('modelos3d', Modelo3DViewSet, basename='modelo3d')

urlpatterns = [
    path('', include(router.urls)),
]