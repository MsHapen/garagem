from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated
from Garagem.models import Veiculo, Marca, Acessorio, Cor
from Garagem.serializers import VeiculoSerializer, MarcaSerializer, AcessorioSerializer, CorSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    #permission_classes = [IsAuthenticated]

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
