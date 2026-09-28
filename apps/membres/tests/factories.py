import factory

from apps.membres.models import Membre


class MembreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membre

    nom = factory.Faker("last_name")
    prenom = factory.Faker("first_name")
    email = factory.Sequence(lambda n: f"membre{n}@exemple.com")
    telephone = "+22370000000"
    actif = True
