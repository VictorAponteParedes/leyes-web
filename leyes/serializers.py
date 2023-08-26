from rest_framework import serializers

from .models import *

class CasoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caso
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = "__all__"


class AbogadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abogado
        fields = "__all__"

