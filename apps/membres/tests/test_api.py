import pytest
from rest_framework.test import APIClient

from apps.membres.tests.factories import MembreFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


def test_creer_membre(client):
    payload = {"nom": "traoré", "prenom": "awa", "email": "Awa@Exemple.com"}
    response = client.post("/api/v1/membres/", payload)
    assert response.status_code == 201
    assert response.data["nom"] == "Traoré"
    assert response.data["email"] == "awa@exemple.com"


def test_creer_membre_email_invalide(client):
    payload = {"nom": "Diallo", "prenom": "Moussa", "email": "pas-un-email"}
    response = client.post("/api/v1/membres/", payload)
    assert response.status_code == 400


def test_creer_membre_email_en_doublon_meme_casse_differente(client):
    MembreFactory(email="awa@exemple.com")
    payload = {"nom": "Autre", "prenom": "Awa", "email": "AWA@exemple.com"}
    response = client.post("/api/v1/membres/", payload)
    assert response.status_code == 400


def test_modifier_membre_garde_son_propre_email(client):
    membre = MembreFactory(email="awa@exemple.com")
    response = client.patch(f"/api/v1/membres/{membre.id}/", {"nom": "Nouveau"})
    assert response.status_code == 200


def test_desactiver_membre(client):
    membre = MembreFactory()
    response = client.patch(f"/api/v1/membres/{membre.id}/", {"actif": False})
    assert response.data["actif"] is False


def test_recherche_par_nom(client):
    MembreFactory(nom="Traoré")
    MembreFactory(nom="Diallo")
    response = client.get("/api/v1/membres/?search=Traoré")
    assert response.data["count"] == 1
