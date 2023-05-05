from rest_framework.viewsets import ModelViewSet

from Garagem.models import Veiculo, Marca, Acessorio, Cor
from Garagem.serializers import VeiculoSerializer, MarcaSerializer, AcessorioSerializer, CorSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer