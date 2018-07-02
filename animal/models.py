import datetime
from client.models import Client
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


MALE = 'male'
FEMALE = 'female'
SEX_ANSWER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)

NO = 'no'
YES = 'yes'
YES_NO_ANSWER = (
    (NO, _('No')),
    (YES, _('Yes')),
)

LONG = 'long'
SHORT = 'short'
FUR_ANSWER = (
    (LONG, _('Long')),
    (SHORT, _('Short')),
)


def validate_date_birth(value):
    if value > datetime.date.today():
        raise ValidationError(_('The date of birth can not be greater than the current date.'))


class Specie(models.Model):
    """
    An instance of this class is an animal specie.
    Species registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Specie')
        verbose_name_plural = _('Species')
        ordering = ('name', )


class Breed(models.Model):
    """
    An instance of this class is a type of breed.
    Breeds registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)
    specie = models.ForeignKey(Specie, verbose_name=_('Specie'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Breed')
        verbose_name_plural = _('Breeds')
        ordering = ('name', )


class Color(models.Model):
    """
    An instance of this class is a type of color for a specific specie.
    Colors registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'    Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)
    specie = models.ForeignKey(Specie, verbose_name=_('Specie'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ('name', )


class Animal(models.Model):
    """
    An instance of this class represents a pet from a customer.

    '__str__'		Returns the name.
    'age'	        Calculates the age according to the date of birth and the current date.
    """
    owner = models.ForeignKey(Client)
    specie = models.ForeignKey(Specie)
    breed = models.ForeignKey(Breed)
    color = models.ForeignKey(Color, blank=True, null=True)
    fur = models.CharField(max_length=5, choices=FUR_ANSWER, blank=True, default=None)
    animal_name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True, validators=[validate_date_birth])
    sex = models.CharField(max_length=6, choices=SEX_ANSWER, blank=True)
    spay_neuter = models.CharField(max_length=3, choices=YES_NO_ANSWER, blank=True)
    spay_neuter_date = models.CharField(max_length=100, blank=True)
    microchip = models.CharField(max_length=50, blank=True)
    dead = models.CharField(max_length=3, choices=YES_NO_ANSWER, blank=True, default=NO)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.animal_name

    def age(self):
        if self.birthdate:
            return int((datetime.date.today() - self.birthdate).days / 365)
        else:
            return None
