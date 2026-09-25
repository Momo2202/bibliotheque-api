from rest_framework import serializers

from .models import Categorie


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ["id", "nom", "description", "date_creation", "date_modification"]
        read_only_fields = ["id", "date_creation", "date_modification"]
