from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import LivreFilter
from .models import Livre
from .serializers import LivreSerializer


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.select_related("categorie").all()
    serializer_class = LivreSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = LivreFilter
    search_fields = ["titre", "auteur", "isbn"]
    ordering_fields = ["titre", "annee_publication", "date_creation"]
