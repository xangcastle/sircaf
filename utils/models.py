from django.db import models
from grappelli_extras.models import base


class Brand(base):
    name = models.CharField(max_length=65, verbose_name="marca")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "marca"


class Country(base):
    name = models.CharField(max_length=65, verbose_name="pais")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "pais"
        verbose_name_plural = "paises"


class Status(base):
    name = models.CharField(max_length=65, verbose_name="estado")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "estado"
