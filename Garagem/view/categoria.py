from rest_framework.viewsets import ModelViewSet
from .categoria import Categoria
from .categoria import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer