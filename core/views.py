from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Filamento, Modelo3D
from .serializers import FilamentoSerializer, Modelo3DSerializer

class FilamentoViewSet(viewsets.ModelViewSet):
    queryset = Filamento.objects.all()
    serializer_class = FilamentoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['tipo', 'em_estoque']  # Permite filtrar por tipo ou stock
    search_fields = ['nome', 'cor']           # Permite pesquisar por nome ou cor

class Modelo3DViewSet(viewsets.ModelViewSet):
    queryset = Modelo3D.objects.all()
    serializer_class = Modelo3DSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['filamento']          # Permite filtrar pelo ID do filamento
    search_fields = ['nome', 'descricao']     # Permite pesquisar por nome ou descrição