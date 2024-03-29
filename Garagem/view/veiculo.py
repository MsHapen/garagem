from rest_framework.viewsets import ModelViewSet
from .veiculo import Veiculo
from .veiculo import VeiculoDetailSerializer, VeiculoListSerializer, VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_classes = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, VeiculoSerializer)