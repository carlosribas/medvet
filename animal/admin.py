# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from animal.models import Breed, Color, Specie


admin.site.register(Breed)
admin.site.register(Color)
admin.site.register(Specie)
