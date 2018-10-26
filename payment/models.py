# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


ONE = '1x'
TWO = '2x'
THREE = '3x'
FOUR = '4x'
FIVE = '5x'
SIX = '6x'
PAYMENT_OPTIONS = (
    (ONE, '1x'),
    (TWO, '2x'),
    (THREE, '3x'),
    (FOUR, '4x'),
    (FIVE, '5x'),
    (SIX, '6x'),
)


class PaymentMethod(models.Model):
    """
    An instance of this class is a payment method.
    Registration of the payment method will be done via Django Admin.

    '__str__'		Returns the name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PaymentRegister(models.Model):
    """
    An instance of this class is the payment register of one or more services.
    """
    installment = models.CharField(max_length=2, choices=PAYMENT_OPTIONS, default=ONE)
    discount_or_increase = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    installment_value = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)


class Payment(models.Model):
    """
    Inline fields for the payment register.
    """
    payment_register = models.ForeignKey(PaymentRegister)
    payment_method = models.ForeignKey(PaymentMethod)
    date = models.DateField()
