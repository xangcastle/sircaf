from django.db import models
from grappelli_extras.models import base


class Group(base):
    name = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.name


INPUT_TYPES = (
    ('TEXT', 'TEXT'),
)


class GroupField(base):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=65, verbose_name="nombre en la base de datos")
    label = models.CharField(max_length=65, verbose_name="etiqueta para el usuario")
    input_type = models.CharField(max_length=4, choices=INPUT_TYPES)

    def __str__(self):
        return self.name


class Brand(base):
    name = models.CharField(max_length=65, verbose_name="marca")

    def __str__(self):
        return self.name


class Country(base):
    name = models.CharField(max_length=65, verbose_name="pais")

    def __str__(self):
        return self.name


class Area(base):
    name = models.CharField(max_length=65, verbose_name="nombre")
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL,
                                verbose_name="pais")

    def __str__(self):
        return self.name


class Status(base):
    name = models.CharField(max_length=65, verbose_name="estado")

    def __str__(self):
        return self.name


class Active(base):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    code = models.CharField(max_length=25, null=True, verbose_name="código",
                            unique=True)
    description = models.CharField(max_length=255, null=True, verbose_name="descripción del bien")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="marca")
    model_name = models.CharField(max_length=65, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="estado")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="area", null=True)
    serial = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.code



