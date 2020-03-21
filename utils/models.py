from django.db import models
from grappelli_extras.models import base


class Brand(base):
    name = models.CharField(max_length=65, verbose_name="marca")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "marca"


class Status(base):
    name = models.CharField(max_length=65, verbose_name="estado")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "estado"


class Group(base):
    name = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "grupo"


INPUT_TYPES = (
    ('TEXT', 'TEXT'),
)


class GroupField(base):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="fields")
    name = models.CharField(max_length=65, verbose_name="nombre en la base de datos")
    label = models.CharField(max_length=65, verbose_name="etiqueta para el usuario")
    input_type = models.CharField(max_length=4, choices=INPUT_TYPES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "campo"


class Area(base):
    name = models.CharField(max_length=65, verbose_name="nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "área"
