from rest_framework import serializers
from ..models import Cultura, Bandeja, Plantio, Notificacao

class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'

class BandejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeja
        fields = '__all__'

class PlantioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantio
        fields = '__all__'
    # Inclua validadores personalizados, se necessário

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'