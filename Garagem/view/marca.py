from rest_framework.viewsets import ModelViewSet
from .marca import Marca
from .marca import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer