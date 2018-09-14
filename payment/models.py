# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models

from services.models import Service, ConsultationType, ExamType, VaccineType, SurgicalProcedure


class PaymentMethod(models.Model):
    """
        An instance of this class is a payment method.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
        An instance of this class is a payment of a service.
    """
    service = models.ForeignKey(Service)
    payment_method = models.ForeignKey(PaymentMethod)
    date = models.DateField(default=datetime.date.today)
    discount_or_increase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)
