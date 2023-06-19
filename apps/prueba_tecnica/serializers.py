from rest_framework import serializers

from .models import Medicion


class MedicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = "__all__"
