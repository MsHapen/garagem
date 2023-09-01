from rest_framework.viewsets import ModelViewSet
from .cor import Cor
from .cor import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer