# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from solo.admin import SingletonModelAdmin

from configuration.models import Document, Image, Page


admin.site.register(Document, SingletonModelAdmin)
admin.site.register(Image, SingletonModelAdmin)
admin.site.register(Page, SingletonModelAdmin)
