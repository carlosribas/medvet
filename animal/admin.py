from forms import *
from django.contrib import admin
from animal.models import *


admin.site.register(Specie)


class ColorAdmin(admin.ModelAdmin):
    fields = ['specie', 'name']
    list_display = ('specie', 'name')
    list_display_links = ('name',)
    ordering = ('specie',)

admin.site.register(Color, ColorAdmin)


class BreedAdmin(admin.ModelAdmin):
    fields = ['specie', 'name']
    list_display = ('specie', 'name')
    list_display_links = ('name',)
    ordering = ('specie',)

admin.site.register(Breed, BreedAdmin)


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = (
                 (None, {
                     'fields': ('owner', 'specie', 'color', 'breed', 'animal_name', 'sex', 'spay_neuter',
                                'spay_neuter_date', 'birthdate', 'microchip', 'dead', 'note'),
                 }),
    )
    list_display = ('owner', 'animal_name', 'sex', 'spay_neuter', 'birthdate')
    list_display_links = ('animal_name', )
    search_fields = ['owner', 'animal_name', 'specie']
    form = AnimalAdminForm

admin.site.register(Animal, AnimalAdmin)
