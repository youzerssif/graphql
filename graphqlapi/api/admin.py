from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'notes', 'category')
    raw_id_fields = ('category',)
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Ingredient, IngredientAdmin)
