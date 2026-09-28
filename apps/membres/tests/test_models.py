import pytest
from django.db import IntegrityError

from apps.membres.tests.factories import MembreFactory

pytestmark = pytest.mark.django_db


def test_str_retourne_prenom_et_nom():
    membre = MembreFactory(prenom="Awa", nom="Traoré")
    assert str(membre) == "Awa Traoré"


def test_email_doit_etre_unique():
    MembreFactory(email="awa@exemple.com")
    with pytest.raises(IntegrityError):
        MembreFactory(email="awa@exemple.com")


def test_membre_actif_par_defaut():
    membre = MembreFactory()
    assert membre.actif is True
