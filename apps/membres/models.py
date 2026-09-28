from django.db import models
from django.utils import timezone

from apps.core.models import BaseModel


class Membre(BaseModel):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(
        max_length=20,
        blank=True,
    )
    date_inscription = models.DateField(default=timezone.localdate)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["nom", "prenom"]
        indexes = [models.Index(fields=["nom", "prenom"])]

    def __str__(self):
        return f"{self.prenom} {self.nom}"
