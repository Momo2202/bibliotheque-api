import factory

from apps.categories.tests.factories import CategorieFactory
from apps.livres.models import Livre


class LivreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Livre

    titre = factory.Sequence(lambda n: f"Livre {n} ")
    auteur = factory.Faker("name")
    isbn = factory.Sequence(lambda n: f"{10000000000 + n}")
    annee_publication = 2020
    exemplaires_total = 3
    exemplaires_disponible = 3
    categorie = factory.SubFactory(CategorieFactory)
