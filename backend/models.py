from django.db import models
from grappelli_extras.models import base
from django.contrib.auth.models import User
from utils.models import *


class Supplier(base):
    name = models.CharField(max_length=300, verbose_name="nombre")
    ruc = models.CharField(max_length=14, verbose_name="número ruc")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"
        app_label = "purchase"


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

    purchase_date = models.DateField(null=True, blank=True)
    dispose_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=165, null=True, blank=True)
    user_function = models.CharField(max_length=165, null=True, blank=True)
    leasing = models.CharField(max_length=25, null=True, blank=True)

    info = models.CharField(max_length=10000, null=True, blank=True, verbose_name="información adicional")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "activo"
        verbose_name_plural = "activo fijo"


class DocumentType(models.IntegerChoices):
    PURCHASE = 1, "Orden de compra"
    INCOMING = 2, "Orden de entrada"
    OUTCOMING = 3, "Orden de salida"
    MAINTENANCE = 4, "Mantenimiento"
    UNACTIVE = 5, "Baja"


class Translate(base):
    """
    cabecera del documento de traslado
    """
    document_type = models.PositiveSmallIntegerField(choices=DocumentType.choices, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    number = models.CharField(max_length=6, null=True, blank=True,
                              verbose_name="número")
    date_time = models.DateTimeField(verbose_name="fecha y hora")
    origin_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="origin_area",
                                    verbose_name="area que envia", null=True, blank=True)
    origin_person = models.CharField(max_length=125, verbose_name="persona que envia", null=True, blank=True)
    origin_charge = models.CharField(max_length=125, verbose_name="cargo de la persona que envia", null=True,
                                     blank=True)
    destiny_area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="destiny_area",
                                     verbose_name="area que recibe", null=True, blank=True)
    destiny_person = models.CharField(max_length=125, verbose_name="persona que recibe", null=True, blank=True)
    destiny_charge = models.CharField(max_length=125, verbose_name="cargo de la persona que recibe", null=True,
                                      blank=True)

    comments = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.number

    def items(self):
        return TranslateItem.objects.filter(translate=self)

    class Meta:
        verbose_name = "traslado"


class TranslateItem(base):
    """
    cada item en la hoja de traslado
    """
    translate = models.ForeignKey(Translate, on_delete=models.CASCADE, related_name="items")
    active = models.ForeignKey(Active, on_delete=models.CASCADE, related_name="translates",
                               verbose_name="activo")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="estado")
    comments = models.CharField(max_length=250, null=True, blank=True, verbose_name="comentarios")

    def __str__(self):
        return self.active.description

    class Meta:
        verbose_name = "item"


class PurchaseManager(models.Manager):
    def get_queryset(self):
        return super(PurchaseManager, self).get_queryset().filter(document_type=DocumentType.PURCHASE)


class IncomingManager(models.Manager):
    def get_queryset(self):
        return super(IncomingManager, self).get_queryset().filter(document_type=DocumentType.INCOMING)


class OutcomingManager(models.Manager):
    def get_queryset(self):
        return super(OutcomingManager, self).get_queryset().filter(document_type=DocumentType.OUTCOMING)


class MaintananceManager(models.Manager):
    def get_queryset(self):
        return super(MaintananceManager, self).get_queryset().filter(document_type=DocumentType.MAINTENANCE)


class UnActiveManager(models.Manager):
    def get_queryset(self):
        return super(UnActiveManager, self).get_queryset().filter(document_type=DocumentType.UNACTIVE)


class Purchase(Translate):
    objects = PurchaseManager()

    class Meta:
        proxy = True
        verbose_name = "orden de compra"
        verbose_name_plural = "ordenes de compra"
        app_label = "purchase"

    def save(self, *args, **kwargs):
        self.document_type = DocumentType.PURCHASE
        super(Purchase, self).save(*args, **kwargs)


class Incoming(Translate):
    objects = IncomingManager()

    class Meta:
        proxy = True
        verbose_name = "entrada"

    def save(self, *args, **kwargs):
        self.document_type = DocumentType.INCOMING
        super(Incoming, self).save(*args, **kwargs)


class Outcoming(Translate):
    objects = OutcomingManager()

    class Meta:
        proxy = True
        verbose_name = "salida"

    def save(self, *args, **kwargs):
        self.document_type = DocumentType.OUTCOMING
        super(Outcoming, self).save(*args, **kwargs)


class Maintanance(Translate):
    objects = MaintananceManager()

    class Meta:
        proxy = True
        verbose_name = "matenimiento"

    def save(self, *args, **kwargs):
        self.document_type = DocumentType.MAINTENANCE
        super(Maintanance, self).save(*args, **kwargs)


class UnActive(Translate):
    objects = UnActiveManager()

    class Meta:
        proxy = True
        verbose_name = "orden de baja"
        verbose_name_plural = "dar de baja"

    def save(self, *args, **kwargs):
        self.document_type = DocumentType.UNACTIVE
        super(UnActive, self).save(*args, **kwargs)


class Inventory(base):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateField(verbose_name="fecha de inventario")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="area de levantamiento", null=True,
                             blank=True)

    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "levantar de inventario"

    def items(self):
        return InventoryItem.objects.filter(inventory=self)


class InventoryItem(base):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    asset = models.ForeignKey(Active, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    comments = models.CharField(max_length=250, null=True, blank=True, verbose_name="comentarios")
