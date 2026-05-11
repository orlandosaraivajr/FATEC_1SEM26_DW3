from rest_framework import serializers
from .models import FeriadoModel

class FeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeriadoModel
        fields = ['id', 'nome', 'dia', 'mes', 'modificado_em']