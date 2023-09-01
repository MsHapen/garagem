from django.db import models
from models import Cor,Acessorio,Marca

class Veiculo(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True ,default="")
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    ano = models.IntegerField(null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name="veiculos",
        default=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.marca} ({self.descricao})"

    class Meta:
        verbose_name = "Veículo"