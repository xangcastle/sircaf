from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class GroupFieldTabular(admin.TabularInline):
    model = GroupField
    extra = 0
    classes = ('grp-collapse', 'grp-open')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = [GroupFieldTabular, ]


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Area)
class AreaAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')


@admin.register(Active)
class ActiveAdmin(ImportExportModelAdmin):
    list_display = ('code', 'brand', 'model_name', 'serial', 'status', 'group')
    search_fields = ('code', 'description', 'brand__name', 'model_name', 'serial')
    list_filter = ('group', 'area', 'brand', 'status')

    fieldsets = [
        ('Información general del activo', {
            'classes': ('grp-collapse', 'grp-open'),
            'fields': (
                ('code', 'description'),
                ('group', 'serial'),
                ('brand', 'model_name'),
                ('area', 'status'),
            )
        })
    ]

