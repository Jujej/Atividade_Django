from django.shortcuts import render
from rest_framework import viewsets
from .models import Filamento, Modelo3D
from .serializers import FilamentoSerializer, Modelo3DSerializer

class FilamentoViewSet(viewsets.ModelViewSet):
    queryset = Filamento.objects.all()
    serializer_class = FilamentoSerializer

class Modelo3DViewSet(viewsets.ModelViewSet):
    queryset = Modelo3D.objects.all()
    serializer_class = Modelo3DSerializer