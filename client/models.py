from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from validation import CPF


def validate_cpf(value):
    """
    Checks if the CPF is valid

    """
    validation = CPF(value)
    if not validation.isValid():
        raise ValidationError(_('%s is not valid CPF') % value)


class Client(models.Model):
    """
    An instance of this class represents a client.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)
    rg = models.CharField(_('RG'), max_length=12, blank=True)
    cpf = models.CharField(_('CPF'), blank=True, max_length=15, validators=[validate_cpf])
    email = models.EmailField(_('E-mail'), blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=15, blank=True)
    cellphone = models.CharField(_('Cell Phone'), max_length=15, blank=True)
    zipcode = models.CharField(_('Zip Code'), max_length=9, blank=True)
    street = models.CharField(_('Address'), max_length=255, blank=True)
    street_complement = models.CharField(_('Complement'), max_length=255, blank=True)
    number = models.PositiveIntegerField(_('Number'), blank=True, null=True)
    district = models.CharField(_('District'), max_length=255, blank=True)
    city = models.CharField(_('City'), max_length=255, blank=True)
    state = models.CharField(_('State'), max_length=255, blank=True)
    country = CountryField(_('Country'), blank=True, default='BR')
    note = models.CharField(_('Note'), max_length=255, blank=True)

    # Returns the name 
    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        ordering = ('name', )


class ClientContact(models.Model):
    """
    An instance of this class represents a contact of client.

    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    client_name = models.ForeignKey(Client)
    name = models.CharField(_('Name'), max_length=255, blank=True)
    phone = models.CharField(_("Phone"), max_length=15, blank=True)
    cellphone = models.CharField(_('Cell Phone'), max_length=15, blank=True)

    class Meta:
        verbose_name = _('Client contact')
        verbose_name_plural = _('Client contacts')
