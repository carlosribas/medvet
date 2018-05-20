import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from animal.models import Animal


BODY_CONDITION = (
    ('0', _('1 - Very thin')),
    ('1', _('2 - Underweight')),
    ('2', _('3 - Ideal weight')),
    ('3', _('4 - Overweight')),
    ('4', _('5 - Obese')),
)

DEFAULT_ANSWER = (
    ('normal', _('Normal')),
    ('abnormal', _('Abnormal')),
)

DEHYDRATED_ANSWER = (
    ('no_dehydration', _('No dehydration')),
    ('reports_loss_of_liquids', _('Less than 5% - Reports loss of liquids')),
    ('mild', _('5 to 6% - Mild')),
    ('moderate', _('7 to 9% - Moderate')),
    ('severe', _('10 to 12% - Severe')),
    ('hypovolemic_shock', _('12 to 15% - Hypovolemic shock')),
)

MUCOUS_ANSWER = (
    ('pink', _('Pink')),
    ('blue', _('Blue')),
    ('pale', _('Pale')),
    ('icteric', _('Icteric')),
    ('congested', _('Congested')),
)


class ConsultationType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class SurgicalProcedure(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class VaccineType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ExamType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class AmbulatoryService(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Service(models.Model):
    SERVIVE_TYPES = (
        ("consultation", _("Consultation")),
        ("surgery", _("Surgical procedure")),
        ("vaccine", _("Vaccine")),
        ("exams", _("Exams")),
        ("ambulatory", _("Ambulatory services")),
    )

    animal = models.ForeignKey(Animal)
    service_type = models.CharField(max_length=20, choices=SERVIVE_TYPES)
    date = models.DateTimeField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        self.animal.save()


class Consultation(Service):
    consultation_type = models.ForeignKey(ConsultationType)
    title = models.CharField(_('Title'), max_length=255, blank=True)
    temperature = models.CharField(_('Temperature'), max_length=3, blank=True)
    bodyweight = models.CharField(_('Bodyweight'), max_length=10, blank=True)
    body_condition = models.CharField(_('Body Condition Score'), max_length=1, choices=BODY_CONDITION, blank=True)
    hydration = models.CharField(_('Skin Tenting'), max_length=25, choices=DEHYDRATED_ANSWER, blank=True)
    mucous_membrane = models.CharField(_('Mucous Membrane'), max_length=10, choices=MUCOUS_ANSWER, blank=True)
    palpable_thyroid = models.CharField(_('Palpable Thyroid'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    palpable_thyroid_note = models.CharField(_('Note'), max_length=255, blank=True)
    auscultation = models.CharField(_('Auscultation'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    auscultation_note = models.CharField(_('Note'), max_length=255, blank=True)
    abdominal_palpation = models.CharField(_('Abdominal Palpation'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    abdominal_palpation_note = models.CharField(_('Note'), max_length=255, blank=True)
    additional_findings = models.TextField(_('Note'), blank=True)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Surgery(Service):
    procedure_type = models.ForeignKey(SurgicalProcedure)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Vaccine(Service):
    vaccine_type = models.ForeignKey(VaccineType)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Exams(Service):
    exam_type = models.ForeignKey(ExamType)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Ambulatory(Service):
    ambulatory_service_type = models.ForeignKey(AmbulatoryService)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)