# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solo.admin import SingletonModelAdmin

from models import Document, Image


admin.site.register(Document, SingletonModelAdmin)
admin.site.register(Image, SingletonModelAdmin)
