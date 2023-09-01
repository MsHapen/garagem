from rest_framework.viewsets import ModelViewSet
from .acessorio import Acessorio
from .acessorio import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer