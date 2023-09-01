from django.db import models

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veículo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veículo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veículo")
    ano = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    Acessorio = models.ManyToManyField(Acessorio, related_name="acessórios")

    def __str__(self):
        return f"{self.marca} - {self.categoria} - {self.cor} - {self.ano} - {self.preco}"
    
    class Meta:
        verbose_name = "Veículo"