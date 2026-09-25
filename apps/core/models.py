from django.db import models


# Create your models here.
class BaseModel(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
