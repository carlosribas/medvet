from animal.models import Animal
from client.models import Client
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Payment(models.Model):
    """
    An instance of this class is a payment of a set of services.

    '__unicode__'		Returns the date.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by date.
    """
    owner = models.ForeignKey(Client, verbose_name=_('Owner'))
    date = models.DateField(_('Date'))
    status = models.NullBooleanField(_('Status'))
    total = models.DecimalField(_('Total'), max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(_('Balance'), max_digits=10, decimal_places=2, blank=True, null=True)

    # Returns the info about the payment
    def __unicode__(self):
        return u'%s - %s - %s' % (self.owner, self.date, self.total)

    # Description of the model / Sort by animal name
    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ('-date', 'owner')

    def save(self, *args, **kwargs):
        items = ServiceItem.objects.filter(payment=self.pk)
        total = 0
        for item in items:
            value = item.value
            total += value
        self.total = total
        super(Payment, self).save(*args, **kwargs)


class ServiceType(models.Model):
    """
    An instance of this class is a type of service.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model / Sort by name
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ('name', )


class ServiceItem(models.Model):
    """
    An instance of this class is a service.

    """
    payment = models.ForeignKey(Payment, verbose_name=_('Payment'))
    animal = models.ForeignKey(Animal, verbose_name=_("Animal's Name"))
    type = models.ForeignKey(ServiceType, verbose_name=_('Type'))
    value = models.DecimalField(_('Value'), max_digits=10, decimal_places=2)
    status = models.NullBooleanField(_('Status'))
