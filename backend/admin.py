from django.contrib import admin
from .forms import *
from import_export.admin import ImportExportModelAdmin



class GroupFieldTabular(admin.TabularInline):
    model = GroupField
    extra = 0
    classes = ('grp-collapse', 'grp-open')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [GroupFieldTabular, ]


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')


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
                ('leasing', ),
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


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time'
    list_display = ('number', 'date_time', 'origin_area', 'destiny_area', 'user')
    list_filter = ('origin_area', 'destiny_area')
    search_fields = ('number', 'origin_area__name')

    fieldsets = (
        ('Informacón del traslado', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('number', 'date_time'),
                ('origin_area', 'destiny_area'),
                ('origin_person', 'destiny_person'),
                ('origin_charge', 'destiny_charge'),
                ('comments',),
            )
        }),
    )

    inlines = [ItemsTabular, ]

