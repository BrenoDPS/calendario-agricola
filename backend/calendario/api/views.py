from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Cultura, Bandeja, Plantio, Notificacao, Evento, Cidade
from .serializers import (
    CulturaSerializer, 
    BandejaSerializer, 
    PlantioSerializer, 
    NotificacaoSerializer,
    EventoSerializer,
    CidadeSerializer,
)

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer


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


class EventoAPIView(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)