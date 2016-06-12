import datetime
from animal.models import Animal
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Examination(models.Model):
    animal = models.ForeignKey(Animal, verbose_name=_("Animal's Name"))
    date = models.DateField(_('Date'), default=datetime.date.today)

    # Returns the date
    def __unicode__(self):
        return u'%s - %s' % (self.date, self.animal)

    def owner(self):
        return u'%s' % self.animal.owner

    class Meta:
        abstract = True


class ExaminationGroup(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    # Returns the name
    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        abstract = True


class Parasitological(ExaminationGroup):
    class Meta:
        verbose_name = _('Parasitological')


class Hematology(ExaminationGroup):
    class Meta:
        verbose_name = _('Hematology')


class RenalProfile(ExaminationGroup):
    class Meta:
        verbose_name = _('Renal profile')


class HepaticProfile(ExaminationGroup):
    class Meta:
        verbose_name = _('Hepatic profile')


class Proteins(ExaminationGroup):
    class Meta:
        verbose_name = _('Proteins')
        verbose_name_plural = _('Proteins')


class Endocrinology(ExaminationGroup):
    class Meta:
        verbose_name = _('Endocrinology')


class Electrolytes(ExaminationGroup):
    class Meta:
        verbose_name = _('Electrolytes')
        verbose_name_plural = _('Electrolytes')


class Microbiology(ExaminationGroup):
    class Meta:
        verbose_name = _('Microbiology')


class Anatomopathology(ExaminationGroup):
    class Meta:
        verbose_name = _('Anatomopathology')


class Image(ExaminationGroup):
    class Meta:
        verbose_name = _('Image')


class Other(ExaminationGroup):
    class Meta:
        verbose_name = _('Other')


class RequestForExamination(Examination):
    parasitological_exam = models.ForeignKey(Parasitological)
    hematology_exam = models.ForeignKey(Hematology)
    renal_profile_exam = models.ForeignKey(RenalProfile)
    hepatic_profile_exam = models.ForeignKey(HepaticProfile)
    proteins_exam = models.ForeignKey(Proteins)
    endocrinology_exam = models.ForeignKey(Endocrinology)
    electrolytes_exam = models.ForeignKey(Electrolytes)
    microbiology_exam = models.ForeignKey(Microbiology)
    anatomopathology_exam = models.ForeignKey(Anatomopathology)
    image_exam = models.ForeignKey(Image)
    other_exam = models.ForeignKey(Other)

    # Description of the model / Sort by date
    class Meta:
        verbose_name = _('Request for examination')
        verbose_name_plural = _('Requests for examination')
        ordering = ('date', )

#
# class ParasitologicalStool(models.Model):
#     ancylostoma = models.CharField(_('Ancylostoma'), max_length=100)
#     dipillidium = models.CharField(_('Dipylidium'), max_length=100)
#     spirocerca = models.CharField(_('Spirocerca'), max_length=100)
#     toxocara = models.CharField(_('Toxocara'), max_length=100)
#     trichuris = models.CharField(_('Trichuris'), max_length=100)
#     giardia = models.CharField(_('Giardia'), max_length=100)
#     isospora = models.CharField(_('Isospora'), max_length=100)
#     note = models.TextField(_('Note'))
#
#
# class Result(Examination):
#     parasitological_stool = models.ForeignKey(ParasitologicalStool)
#
#     # Description of the model / Sort by date
#     class Meta:
#         verbose_name = _('Result')
#         verbose_name_plural = _('Results')
#         ordering = ('date', )
