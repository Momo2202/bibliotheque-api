import pytest
from django.db import IntegrityError

from apps.categories.tests.factories import CategorieFactory
from apps.livres.tests.factories import LivreFactory

pytestmark = pytest.mark.django_db


def test_isbn_doit_etre_unique():
    LivreFactory(isbn="45678910")
    with pytest.raises(IntegrityError):
        LivreFactory(isbn="45678910")


def test_suppresion_categorie_avec_livres_est_protegee():
    categorie = CategorieFactory()
    LivreFactory(categorie=categorie)
    with pytest.raises(Exception):
        categorie.delete()
