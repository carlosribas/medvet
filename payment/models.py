# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models

from services.models import Service


class Payment(models.Model):
    """
        An instance of this class is a payment of a service.
    """
    service = models.ForeignKey(Service)
    date = models.DateField(default=datetime.date.today)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
