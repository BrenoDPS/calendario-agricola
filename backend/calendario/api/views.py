from rest_framework import viewsets
from ..models import Cultura, Bandeja, Plantio, Notificacao
from .serializers import CulturaSerializer, BandejaSerializer, PlantioSerializer, NotificacaoSerializer

class CulturaViewSet(viewsets.ModelViewSet):
    queryset = Cultura.objects.select_related('nome', 'descricao').all()
    serializer_class = CulturaSerializer

class BandejaViewSet(viewsets.ModelViewSet):
    queryset = Bandeja.objects.select_related('nome', 'descricao').all()
    serializer_class = BandejaSerializer

class PlantioViewSet(viewsets.ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.select_related(
        'plantio', 'mensagem', 'enviada', 'data_notificacao').all()
    serializer_class = NotificacaoSerializer
