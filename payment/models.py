# from django.db import models
# from django.utils.translation import ugettext_lazy as _
#
# from animal.models import Animal
# from client.models import Client
# from physical_examination.models import Examination
#
#
# class Payment(models.Model):
#     """
#     An instance of this class is a payment of a services.
#
#     '__unicode__'		Returns the date.
#     'class Meta'		Sets the description model (singular and plural) and define ordering of data by date.
#     """
#     owner = models.ForeignKey(Client)
#     animal = models.ForeignKey(Animal)
#     service = models.ForeignKey(Examination, related_name='service')
#     date = models.DateField()
#     value = models.DecimalField(max_digits=10, decimal_places=2)
#
#     # Returns the info about the payment
#     def __unicode__(self):
#         return u'%s - %s' % (self.owner, self.date)
#
#     # Description of the model / Sort by animal name
#     class Meta:
#         verbose_name = _('Payment')
#         verbose_name_plural = _('Payments')
#         ordering = ('-date', 'owner')
