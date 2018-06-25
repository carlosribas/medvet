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

EXAM = (
    ('request', _('Request of exam')),
    ('annex', _('Annex of exam')),
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


class ExamCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExamType(models.Model):
    category = models.ForeignKey(ExamCategory)
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
        ("exam", _("Exam")),
        ("ambulatory", _("Ambulatory services")),
    )

    animal = models.ForeignKey(Animal)
    service_type = models.CharField(max_length=20, choices=SERVIVE_TYPES)
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
        self.animal.save()


class Consultation(Service):
    consultation_type = models.ForeignKey(ConsultationType)
    title = models.CharField(max_length=255, blank=True)
    temperature = models.CharField(max_length=3, blank=True)
    bodyweight = models.CharField(max_length=10, blank=True)
    body_condition = models.CharField(max_length=1, choices=BODY_CONDITION, blank=True)
    hydration = models.CharField(max_length=25, choices=DEHYDRATED_ANSWER, blank=True)
    mucous_membrane = models.CharField(max_length=10, choices=MUCOUS_ANSWER, blank=True)
    palpable_thyroid = models.CharField(max_length=10, choices=DEFAULT_ANSWER, blank=True)
    palpable_thyroid_note = models.CharField(max_length=255, blank=True)
    auscultation = models.CharField(max_length=10, choices=DEFAULT_ANSWER, blank=True)
    auscultation_note = models.CharField(max_length=255, blank=True)
    abdominal_palpation = models.CharField(max_length=10, choices=DEFAULT_ANSWER, blank=True)
    abdominal_palpation_note = models.CharField(max_length=255, blank=True)
    additional_findings = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Surgery(Service):
    procedure_type = models.ForeignKey(SurgicalProcedure)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Vaccine(Service):
    vaccine_type = models.ForeignKey(VaccineType)
    vaccine_in_consultation = models.ForeignKey(Consultation, blank=True, null=True)
    lot = models.CharField(max_length=255, blank=True)
    booster = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


def exam_path(instance, filename):
    return 'exams/{0}/{1}/{2}'.format(instance.animal.animal_name, datetime.date.today().strftime('%d-%m-%Y'), filename)


class Exam(Service):
    exam_type = models.ManyToManyField(ExamType)
    exam_in_consultation = models.ForeignKey(Consultation, blank=True, null=True)
    exam_request = models.CharField(max_length=10, choices=EXAM, default=True)
    exam_file = models.FileField(blank=True, null=True, upload_to=exam_path)
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)


class Ambulatory(Service):
    ambulatory_service_type = models.ForeignKey(AmbulatoryService)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)
