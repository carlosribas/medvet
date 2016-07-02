import datetime
from client.models import Client
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


MALE = 'm'
FEMALE = 'f'
SEX_ANSWER = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
)

NO = 'n'
YES = 'y'
SPAY_NEUTER_ANSWER = (
    (NO, _('No')),
    (YES, _('Yes')),
)

LONG = 'l'
SHORT = 's'
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

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Specie')
        verbose_name_plural = _('Species')
        ordering = ('name', )


class Breed(models.Model):
    """
    An instance of this class is a type of breed.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)
    specie = models.ForeignKey(Specie, verbose_name=_('Specie'))

    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Breed')
        verbose_name_plural = _('Breeds')
        ordering = ('name', )


class Color(models.Model):
    """
    An instance of this class is a type of color.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=100)
    specie = models.ForeignKey(Specie, verbose_name=_('Specie'))

    # Returns the name 
    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')
        ordering = ('name', )


class Animal(models.Model):
    """
    An instance of this class represents a pet from a client.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by animal_name.
    """
    owner = models.ForeignKey(Client, verbose_name=_('Owner'))
    specie = models.ForeignKey(Specie, verbose_name=_('Specie'))
    breed = models.ForeignKey(Breed, verbose_name=_('Breed'))
    color = models.ForeignKey(Color, verbose_name=_('Color'))
    fur = models.CharField(_('Fur'), max_length=1, choices=FUR_ANSWER, blank=True, null=True, default=None)
    animal_name = models.CharField(_("Animal's Name"), max_length=100,
                                   error_messages={'required': _('Please enter the name of the pet')})
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True, validators=[validate_date_birth])
    sex = models.CharField(_('Sex'), max_length=1, choices=SEX_ANSWER, blank=True, null=True)
    spay_neuter = models.CharField(_('Spay or Neuter'), max_length=1, choices=SPAY_NEUTER_ANSWER, blank=True,
                                   null=True)
    spay_neuter_date = models.CharField(_('When?'), max_length=100, blank=True, null=True)
    microchip = models.CharField(_('Microchip'), max_length=50, blank=True, null=True)
    dead = models.BooleanField(_('Dead'), default=False)
    note = models.CharField(_('Note'), max_length=255, blank=True, null=True)

    # Returns the name 
    def __unicode__(self):
        return u'%s' % self.animal_name

    # Description of the model / Sort by animal name
    class Meta:
        verbose_name = _('Animal')
        verbose_name_plural = _('Animals')
        ordering = ('animal_name',)
