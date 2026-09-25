import pytest

from apps.categories.tests.factories import CategorieFactory

pytestmark = pytest.mark.django_db


def test_creation_categorie():
    categorie = CategorieFactory(nom="Roman")
    assert categorie.nom == "Roman"
    assert categorie.date_creation is not None


def test_str_retourne_le_nom():
    categorie = CategorieFactory(nom="Poésie")
    assert str(categorie) == "Poésie"
