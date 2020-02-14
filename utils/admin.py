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


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

