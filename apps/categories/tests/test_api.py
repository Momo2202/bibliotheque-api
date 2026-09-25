import pytest
from rest_framework.test import APIClient

from apps.categories.tests.factories import CategorieFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


def test_lister_categories(client):
    CategorieFactory.create_batch(3)
    response = client.get("/api/v1/categories/")
    assert response.status_code == 200
    assert response.data["count"] == 3


def tester_creer_categorie(client):
    payload = {"nom": "Fantasy", "descriptipn": "Univers Imaginaires"}
    response = client.post("/api/v1/categories/", payload)
    assert response.status_code == 201
    assert response.data["nom"] == "Fantasy"


def tester_creer_categorie_nom_deja_existant(client):
    CategorieFactory(nom="Fantasy")
    response = client.post("/api/v1/categories/", {"nom": "Fantasy"})
    assert response.status_code == 400


def test_modifier_categorie(client):
    categorie = CategorieFactory(nom="Ancien nom")
    response = client.patch(f"/api/v1/categories/{categorie.id}/", {"nom": "Nouveau nom"})
    assert response.status_code == 200
    assert response.data["nom"] == "Nouveau nom"


def test_supprimer_categorie(client):
    categorie = CategorieFactory()
    response = client.delete(f"/api/v1/categories/{categorie.id}/")
    assert response.status_code == 204


def test_recherche_categorie(client):
    CategorieFactory(nom="Science-fiction")
    CategorieFactory(nom="Histoire")
    response = client.get("/api/v1/categories/?search=fiction")
    assert response.data["count"] == 1
