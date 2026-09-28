from django.db import models

from apps.categories.models import Categorie
from apps.core.models import BaseModel


class Livre(BaseModel):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    annee_publication = models.PositiveIntegerField()
    exemplaires_total = models.PositiveIntegerField(default=1)
    exemplaires_disponible = models.PositiveIntegerField(default=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, related_name="livres")

    class Meta:
        ordering = ["titre"]
        indexes = [
            models.Index(fields=["titre"]),
            models.Index(fields=["auteur"]),
        ]

    def __str__(self):
        return f"{self.titre} ({self.auteur})"
