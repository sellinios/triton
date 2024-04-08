# vessels/models.py
from django.db import models


class Principal(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()

    def __str__(self):
        return self.name


class Vessel(models.Model):
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    # Other vessel fields...

    def __str__(self):
        return self.name
