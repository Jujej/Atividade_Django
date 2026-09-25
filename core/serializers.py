from rest_framework import serializers
from .models import Filamento, Modelo3D

class FilamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filamento
        fields = '__all__'

class Modelo3DSerializer(serializers.ModelSerializer):
    # Exibe os dados do filamento aninhados na leitura (GET)
    filamento_detalhes = FilamentoSerializer(source='filamento', read_only=True)

    class Meta:
        model = Modelo3D
        fields = [
            'id', 
            'nome', 
            'descricao', 
            'peso_gramas', 
            'tempo_impressao_minutos', 
            'preco_final', 
            'filamento',            # ID do filamento (necessário no POST/PUT)
            'filamento_detalhes'   # Objeto completo do filamento (exibido no GET)
        ]