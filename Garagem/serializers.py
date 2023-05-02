from rest_framework.serializers import ModelSerializer

from Garagem.models import Veiculos

class VeiculosSerializer(ModelSerializer):
    class Meta:
        model = Veiculos
        fields = "__all__"