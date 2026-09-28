from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Membre
from .serializers import MembreSerializer


class MembreViewSet(viewsets.ModelViewSet):
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["nom", "prenom", "email"]
    search_fields = ["nom", "prenom", "email"]
    ordering_fields = ["nom", "date_inscription"]
