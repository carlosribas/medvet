import datetime
from animal.models import Animal
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExamType(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    class Meta:
        abstract = True


class Parasitological(ExamType):
    # Returns the name
    def __unicode__(self):
        return u'%s' % self.name


class Exam(models.Model):
    animal = models.ForeignKey(Animal, verbose_name=_("Animal's Name"))
    date = models.DateField(_('Date'), default=datetime.date.today)
    type_parasitological = models.ForeignKey(Parasitological)

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

