# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from services.models import Service


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
    date = models.DateField()
    discount_or_increase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)
