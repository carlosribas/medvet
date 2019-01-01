from django.contrib import admin

from .models import Manufacturer, Classification, Indication, Group, Presentation, System, UnitOfMeasurement, Drug, \
    DrugDosage


admin.site.register(Manufacturer)
admin.site.register(Classification)
admin.site.register(Indication)
admin.site.register(Group)
admin.site.register(Presentation)
admin.site.register(System)
admin.site.register(UnitOfMeasurement)
admin.site.register(Drug)
admin.site.register(DrugDosage)
