from django.db import models
from grappelli_extras.models import base
from django.contrib.auth.models import User


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


class Area(base):
    name = models.CharField(max_length=65, verbose_name="nombre")
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL,
                                verbose_name="pais")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "área"


class Status(base):
    name = models.CharField(max_length=65, verbose_name="estado")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "estado"


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
    info = models.CharField(max_length=10000, null=True, blank=True, verbose_name="información adicional")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "activo"


class Translate(base):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    number = models.CharField(max_length=6, null=True, blank=True,
                              verbose_name="número")
    date_time = models.DateTimeField(verbose_name="fecha y hora")
    origin_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="origin_area",
                                    verbose_name="area que envia")
    origin_person = models.CharField(max_length=125, verbose_name="persona que envia")
    origin_charge = models.CharField(max_length=125, verbose_name="cargo de la persona que envia")
    destiny_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="destiny_area",
                                     verbose_name="area que recibe")
    destiny_person = models.CharField(max_length=125, verbose_name="persona que recibe")
    destiny_charge = models.CharField(max_length=125, verbose_name="cargo de la persona que recibe")

    comments = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "traslado"


class TranslateItem(base):
    translate = models.ForeignKey(Translate, on_delete=models.CASCADE, related_name="items")
    active = models.ForeignKey(Active, on_delete=models.CASCADE, related_name="translates",
                               verbose_name="activo")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="estado")
    comments = models.CharField(max_length=250, null=True, blank=True, verbose_name="comentarios")

    def __str__(self):
        return self.active.description

    class Meta:
        verbose_name = "item"
