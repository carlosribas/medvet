# -*- coding: UTF-8 -*-
import datetime

from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _

from animal.models import Animal, Specie
from payment.models import PaymentRegister


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

EXAM_TYPE = (
    ('collect', _('Exam conducted')),
    ('request', _('Request of exam')),
    ('annex', _('Attach exam')),
)

CONSULTATION = "Consultation"
VACCINE = "Vaccine"
EXAM = "Exam"

NO = 'no'
YES = 'yes'
YES_NO_ANSWER = (
    (NO, _('No')),
    (YES, _('Yes')),
)


class ConsultationType(models.Model):
    """
    An instance of this class is a type of consultation.
    The creation of this instance will be done via Django Admin.

    '__str__'		Returns the name.
    """
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class VaccineType(models.Model):
    """
    An instance of this class is a type of vaccine.
    The creation of this instance will be done via Django Admin.

    '__str__'		Returns the name.
    """
    vaccine_for = models.ForeignKey(Specie, default=1)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ExamCategory(models.Model):
    """
    An instance of this class is an exam category.
    The creation of this instance will be done via Django Admin.

    '__str__'		Returns the name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExamName(models.Model):
    """
    An instance of this class is a name of an exam.
    The creation of this instance will be done via Django Admin.

    '__str__'		Returns the name.
    """
    category = models.ForeignKey(ExamCategory)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Service(models.Model):
    animal = models.ForeignKey(Animal)
    payment = models.ForeignKey(PaymentRegister, blank=True, null=True)
    service_type = models.CharField(max_length=20)
    date = models.DateField(default=datetime.date.today)
    paid = models.CharField(max_length=3, choices=YES_NO_ANSWER, blank=True, default=NO)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Consultation(Service):
    consultation_type = models.ForeignKey(ConsultationType)
    title = models.CharField(max_length=255, blank=True)
    temperature = models.CharField(max_length=4, blank=True)
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
        self.service_type = CONSULTATION
        self.service_cost = self.consultation_type.price
        super(Service, self).save(*args, **kwargs)


class Vaccine(Service):
    vaccine_type = models.ForeignKey(VaccineType)
    vaccine_in_consultation = models.ForeignKey(Consultation, blank=True, null=True)
    lot = models.CharField(max_length=255, blank=True)
    booster = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.service_type = VACCINE
        self.service_cost = self.vaccine_type.price
        super(Service, self).save(*args, **kwargs)


def exam_path(instance, filename):
    return 'exams/{0}/{1}/{2}'.format(
        instance.animal.animal_name, datetime.date.today().strftime('%d-%m-%Y'), str(filename)
    )


class Exam(Service):
    exam_list = models.ManyToManyField(ExamName)
    exam_in_consultation = models.ForeignKey(Consultation, blank=True, null=True)
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE, default=True)
    exam_file = models.FileField(blank=True, null=True, upload_to=exam_path)
    note = models.TextField(blank=True)

    @property
    def sum_exam(self):
        result = self.exam_list.aggregate(Sum('price'))
        return result['price__sum']

    def save(self, *args, **kwargs):
        self.service_type = EXAM
        if self.exam_type == 'request' or self.exam_type == 'annex':
            self.paid = YES
            self.service_cost = 0
        else:
            self.paid = NO
            self.service_cost = None

        super(Service, self).save(*args, **kwargs)
