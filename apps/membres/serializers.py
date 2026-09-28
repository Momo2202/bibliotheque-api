from rest_framework import serializers

from .models import Membre


class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = [
            "id",
            "nom",
            "prenom",
            "email",
            "telephone",
            "date_inscription",
            "actif",
            "date_creation",
            "date_modification",
        ]

        read_only_fields = ["id", "date_creation", "date_modification"]

    def validate_email(self, value):
        email = value.lower().strip()
        queryset = Membre.objects.filter(email=email)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("Un membre avec cet email existe déja")
        return email

    def validate_nom(self, value):
        return value.strip().title()

    def validate_prenom(self, value):
        return value.strip().title()
