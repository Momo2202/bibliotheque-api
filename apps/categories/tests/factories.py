import factory

from apps.categories.models import Categorie


class CategorieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categorie

    nom = factory.Sequence(lambda n: f"Catégorie {n}")
    description = factory.Faker("sentence")
