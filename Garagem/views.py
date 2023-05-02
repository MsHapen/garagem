from rest_framework.viewsets import ModelViewSet

from Garagem.models import Veiculo
from Garagem.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
