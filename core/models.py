from django.db import models

class Filamento(models.Model):
    TIPO_CHOICES = [
        ('PLA', 'PLA'),
        ('ABS', 'ABS'),
        ('PETG', 'PETG'),
        ('TPU', 'TPU (Flexível)'),
        ('RESINA', 'Resina UV'),
    ]

    nome = models.CharField(max_length=100) # Ex: PLA Premium Preto
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    cor = models.CharField(max_length=50) # Ex: Preto Fosco
    preco_por_grama = models.DecimalField(max_digits=6, decimal_places=4) # Ex: 0.1500 (R$ 0,15 por grama)
    em_estoque = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.cor})"


class Modelo3D(models.Model):
    nome = models.CharField(max_length=150) # Ex: Suporte de Headset
    descricao = models.TextField(blank=True, null=True)
    peso_gramas = models.IntegerField() # Ex: 120 (gramas de material)
    tempo_impressao_minutos = models.IntegerField() # Ex: 240 (minutos)
    preco_final = models.DecimalField(max_digits=8, decimal_places=2) # Ex: 45.00
    
    # Relacionamento 1:N (Um filamento pode ser usado em vários modelos 3D)
    filamento = models.ForeignKey(
        Filamento, 
        on_delete=models.CASCADE, 
        related_name='modelos'
    )

    def __str__(self):
        return self.nome