from django.db import models

class Marca(models.Model):

    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50,null=False, blank=True)

    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    marca = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name="marca")
    categoria = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name="categoria")
    cor = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name="cor")
    ano = models.IntegerField(null=True default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)

    def __str__(self):
        return self.marca