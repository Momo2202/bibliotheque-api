from rest_framework import serializers

from .models import Livre


class LivreSerializer(serializers.ModelSerializer):
    categorie_nom = serializers.CharField(source="categorie.nom", read_only=True)

    class Meta:
        model = Livre
        fields = [
            "id",
            "titre",
            "auteur",
            "isbn",
            "annee_publication",
            "exemplaires_total",
            "exemplaires_disponible",
            "categorie",
            "categorie_nom",
            "date_creation",
            "date_modification",
        ]

        read_only_fields = ["id", "exemplaires_disponible", "date_creation", "date_modification"]

        def validate(self, data):
            total = data.get("exemplaires_total", getattr(self.instance, "exemplaires_total", None))
            if total is not None and total <= 1:
                raise serializers.ValidationError(
                    {"exemplaires_total": "Le nombre doit etre au moins 1"}
                )
            return data

        def create(self, validated_data):
            self.validate["exemplaires_disponible"] = validated_data["exemple_total"]
            return super().create(validated_data)
