from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
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
    rg = models.CharField(_('RG'), max_length=12, blank=True, null=True)
    cpf = models.CharField(_('CPF'), blank=True, null=True, max_length=15, validators=[validate_cpf])
    email = models.EmailField(_('E-mail'), blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=15, blank=True, null=True)
    cellphone = models.CharField(_('Cell Phone'), max_length=15, blank=True, null=True)
    zipcode = models.CharField(_('Zip Code'), max_length=9, blank=True, null=True)
    street = models.CharField(_('Address'), max_length=255, blank=True, null=True)
    street_complement = models.CharField(_('Complement'), max_length=255, blank=True, null=True)
    number = models.PositiveIntegerField(_('Number'), blank=True, null=True)
    district = models.CharField(_('District'), max_length=255, blank=True, null=True)
    city = models.CharField(_('City'), max_length=255, blank=True, null=True)
    state = models.CharField(_('State'), max_length=255, blank=True, null=True)
    note = models.CharField(_('Note'), max_length=255, blank=True, null=True)
    another_responsible = models.CharField(_('Another Responsible'), max_length=255, blank=True, null=True)
    another_responsible_phone = models.CharField(_("Another Responsible's Phone"), max_length=15, blank=True, null=True)

    # Returns the name 
    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')
        ordering = ('name', )
