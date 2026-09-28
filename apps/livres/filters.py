import django_filters

from .models import Livre


class LivreFilter(django_filters.FilterSet):
    categorie = django_filters.filters.NumberFilter(field_name="categorie__id")
    disponible = django_filters.BooleanFilter(method="filtrer_disponible")
    annee_min = django_filters.NumberFilter(field_name="annee_publication", lookup_expr="gte")
    annee_max = django_filters.NumberFilter(field_name="annee_publication", lookup_expr="lte")

    class Meta:
        model = Livre
        fields = ["categorie", "disponible", "annee_min", "annee_max"]

        def filtrer_disponible(self, queryset, name, value):
            if value:
                return queryset.filter(exemplaires_disponible__gt=0)
            return queryset.filter(exemplaires_disponible=0)
