# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from payment.models import PaymentMethod

admin.site.register(PaymentMethod)
