import pytest
from rest_framework.test import APIClient

from apps.categories.tests.factories import CategorieFactory
from apps.livres.tests.factories import LivreFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


def test_filtrer_par_categorie(client):
    cat_a = CategorieFactory()
    cat_b = CategorieFactory()
    LivreFactory(categorie=cat_a)
    LivreFactory(categorie=cat_b)
    response = client.get(f"/api/v1/livres/?categorie={cat_a.id}")
    assert response.data["count"] == 1


def test_filtrer_par_plage_annees(client):
    LivreFactory(annee_publication=1990)
    LivreFactory(annee_publication=2020)
    response = client.get("/api/v1/livres/?annee_min=2000")
    assert response.data["count"] == 1


def test_recherche_par_auteur(client):
    LivreFactory(auteur="Isaac Asimov")
    LivreFactory(auteur="Frank Herbert")
    response = client.get("/api/v1/livres/?search=Asimov")
    assert response.data["count"] == 1
