import datetime
from animal.models import Animal
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExamType(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    # Returns the name
    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        abstract = True


class Parasitological(ExamType):
    class Meta:
        verbose_name = _('Parasitological')


class Hematology(ExamType):
    class Meta:
        verbose_name = _('Hematology')


class RenalProfile(ExamType):
    class Meta:
        verbose_name = _('Renal profile')


class HepaticProfile(ExamType):
    class Meta:
        verbose_name = _('Hepatic profile')


class Proteins(ExamType):
    class Meta:
        verbose_name = _('Proteins')


class Endocrinology(ExamType):
    class Meta:
        verbose_name = _('Endocrinology')


class Electrolytes(ExamType):
    class Meta:
        verbose_name = _('Electrolytes')


class Microbiology(ExamType):
    class Meta:
        verbose_name = _('Microbiology')


class Anatomopathology(ExamType):
    class Meta:
        verbose_name = _('Anatomopathology')


class Image(ExamType):
    class Meta:
        verbose_name = _('Image')


class Exam(models.Model):
    animal = models.ForeignKey(Animal, verbose_name=_("Animal's Name"))
    date = models.DateField(_('Date'), default=datetime.date.today)
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

    # Returns the date
    def __unicode__(self):
        return u'%s - %s' % (self.date, self.animal)

    def owner(self):
        return u'%s' % self.animal.owner

    # Description of the model / Sort by date
    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')
        ordering = ('date', )

