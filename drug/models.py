from django.db import models
from django.utils.translation import ugettext_lazy as _

from animal.models import Specie

HUMAN = 'human'
HUMAN_PEDIATRIC = 'pediatric'
VET = 'vet'
USE_ANSWER = (
    (HUMAN, _('Human')),
    (HUMAN_PEDIATRIC, _('Human pediatric')),
    (VET, _('Vet')),
)


class Manufacturer(models.Model):
    """
    An instance of this class is a drug manufacturer.
    Manufacturer registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')
        ordering = ('name', )


class Classification(models.Model):
    """
    An instance of this class is the classification of a drug.
    The classification record will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Classification')
        verbose_name_plural = _('Classifications')
        ordering = ('name', )


class Indication(models.Model):
    """
    An instance of this class is for which purpose a drug is used.
    The indication record will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Indication')
        verbose_name_plural = _('Indications')
        ordering = ('name', )


class Group(models.Model):
    """
    An instance of this class is a drug group.
    Group registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ('name', )


class Presentation(models.Model):
    """
    An instance of this class is a physical form of the drug (eg. pill, capsule, ...).
    The presentation record will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')
        ordering = ('name', )


class System(models.Model):
    """
    An instance of this class is a unit of measurement system.
    System registration will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('System')
        verbose_name_plural = _('Systems')
        ordering = ('name', )


class UnitOfMeasurement(models.Model):
    """
    An instance of this class is a type of unit of measurement.
    The registration of the unit of measurement will be done via Django Admin.

    '__str__'		Returns the name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by name.
    """
    system = models.ForeignKey(System, verbose_name=_('System'))
    name = models.CharField(_('Name'), max_length=100)
    abbreviation = models.CharField(_('Abbreviation'), max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit of measurement')
        verbose_name_plural = _('Units of measurement')
        ordering = ('name', )


class Drug(models.Model):
    """
    An instance of this class is a drug.
    Drug registration will be done via Django Admin.

    '__str__'		Returns the generic name.
    'class Meta'	Sets the description model (singular and plural) and define ordering of data by generic name.
    """
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    classification = models.ForeignKey(Classification, blank=True, null=True)
    indication = models.ForeignKey(Indication, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    presentation = models.ForeignKey(Presentation, blank=True, null=True)
    generic_name = models.CharField(max_length=150)
    commercial_name = models.CharField(max_length=150, blank=True)
    use = models.CharField(max_length=10, choices=USE_ANSWER, blank=True, default=None)
    value = models.CharField(max_length=10)
    value_unit = models.ForeignKey(UnitOfMeasurement, related_name='drug_value_unit')
    value_for = models.CharField(max_length=10)
    value_for_unit = models.ForeignKey(UnitOfMeasurement, related_name='drug_value_for_unit')

    def __str__(self):
        return self.generic_name

    class Meta:
        verbose_name = _('Drug')
        verbose_name_plural = _('Drugs')
        ordering = ('generic_name', )


class DrugDosage(models.Model):
    """
    An instance of this class is a dosage of a drug for an specific specie.
    Dosage registration will be done via Django Admin.

    'class Meta'	Sets the description model (singular and plural) and define ordering of data by drug.
    """
    drug = models.ForeignKey(Drug)
    specie = models.ForeignKey(Specie)
    value_from = models.CharField(max_length=10)
    value_to = models.CharField(max_length=10, blank=True)
    value_unit = models.ForeignKey(UnitOfMeasurement, related_name='dosage_value_unit')
    value_for = models.CharField(max_length=10, default=1)
    value_for_unit = models.ForeignKey(UnitOfMeasurement, related_name='dosage_value_for_unit')
    periodicity = models.CharField(max_length=10)
    periodicity_unit = models.ForeignKey(UnitOfMeasurement, related_name='dosage_periodicity')
    period = models.CharField(max_length=10)
    period_unit = models.ForeignKey(UnitOfMeasurement, related_name='dosage_period')

    def __str__(self):
        return "%s - %s" % (self.specie, self.drug)

    class Meta:
        verbose_name = _('Drug dosage')
        verbose_name_plural = _('Drugs dosage')
        ordering = ('drug', )
