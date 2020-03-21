from django.contrib import admin
from .forms import *
from import_export.admin import ImportExportModelAdmin


class GroupFieldTabular(admin.TabularInline):
    model = GroupField
    extra = 0
    classes = ('grp-collapse', 'grp-open')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [GroupFieldTabular, ]


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Active)
class ActiveAdmin(ImportExportModelAdmin):
    form = ActiveForm
    list_display = ('code', 'brand', 'model_name', 'serial', 'status', 'group')
    search_fields = ('code', 'description', 'brand__name', 'model_name', 'serial')
    list_filter = ('group', 'area', 'brand', 'status')

    fieldsets = [
        ('Descripción del activo', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('code', 'description'),
                ('group', 'serial'),
                ('brand', 'model_name'),
                ('area', 'status'),
            )
        }),
        ('Información adicional', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('purchase_date', 'dispose_date'),
                ('username', 'user_function'),
                ('leasing',),
            )
        }),
        ('Otros datos', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('info',),
            )
        }),
    ]


class ItemsTabular(admin.TabularInline):
    model = TranslateItem
    classes = ('grp-collapse', 'grp-open')
    fields = ('active', 'status', 'comments')
    extra = 1
    raw_id_fields = ('active',)
    autocomplete_lookup_fields = {
        'fk': ['active'],
    }


@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('origin_area',),
                ('origin_person', 'origin_charge'),
                ('destiny_person', 'destiny_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]


@admin.register(Outcoming)
class OutcomingAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('destiny_area',),
                ('origin_person', 'origin_charge'),
                ('destiny_person', 'destiny_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]


@admin.register(Maintanance)
class MaintananceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('origin_person', 'origin_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('origin_person', 'origin_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]


@admin.register(UnActive)
class UnActiveAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('origin_person', 'origin_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'ruc')
    search_fields = ('name', 'ruc')


class InventoryTabular(admin.TabularInline):
    model = InventoryItem
    classes = ('grp-collapse', 'grp-open')
    fields = ('asset', 'status', 'comments')
    extra = 1
    raw_id_fields = ('asset',)
    autocomplete_lookup_fields = {
        'fk': ['asset'],
    }


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    inlines = [InventoryTabular, ]


