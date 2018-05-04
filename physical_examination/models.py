import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from animal.models import Animal
from client.models import Client

ATTITUDE_ANSWER = (
    ('bright_and_alert', _('Bright and Alert')),
    ('quiet_but_alert', _('Quiet but Alert')),
    ('lethargic', _('Lethargic')),
    ('dull', _('Dull')),
    ('hyperactive', _('Hyperactive')),
    ('other', _('Other')),
)

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

FACE_ANSWER = (
    ('normal', _('Normal')),
    ('head_tilt', _('Head tilt')),
    ('abnormal', _('Abnormal')),
)

MUCOUS_ANSWER = (
    ('pink', _('Pink')),
    ('blue', _('Blue')),
    ('pale', _('Pale')),
    ('icteric', _('Icteric')),
    ('congested', _('Congested')),
)


class ExaminationType(models.Model):
    """
    An instance of this class is an examination type.

    '__unicode__'		Returns the name.
    'class Meta'		Sets the description model (singular and plural).
    """

    name = models.CharField(_('Name'), max_length=255)

    # Returns the name
    def __unicode__(self):
        return u'%s' % self.name

    # Description of the model
    class Meta:
        verbose_name = _('Examination')
        verbose_name_plural = _('Examinations')


class Examination(models.Model):
    """
    An instance of this class is an examination of an animal.

    '__unicode__'		Returns the date.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by date.
    """

    examination_type = models.ForeignKey(ExaminationType, verbose_name=_("Type"))
    title = models.CharField(_('Title'), max_length=255, blank=True)
    animal = models.ForeignKey(Animal, verbose_name=_("Animal's Name"))
    date = models.DateField(_('Date'), default=datetime.date.today)
    temperature = models.CharField(_('Temperature'), max_length=3, blank=True)
    pulse = models.CharField(_('Pulse'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    pulse_note = models.CharField(_('Note'), max_length=255, blank=True)
    respiratory_rate = models.CharField(_('Respiratory Rate'), max_length=10, blank=True)
    bodyweight = models.CharField(_('Bodyweight'), max_length=10, blank=True)
    body_condition = models.CharField(_('Body Condition Score'), max_length=1, choices=BODY_CONDITION, blank=True)
    attitude = models.CharField(_('Attitude'), max_length=20, choices=ATTITUDE_ANSWER, blank=True)
    attitude_note = models.CharField(_('Note'), max_length=255, blank=True)
    face = models.CharField(_('Face'), max_length=10, choices=FACE_ANSWER, blank=True)
    face_note = models.CharField(_('Note'), max_length=255, blank=True)
    eye = models.CharField(_('Eye'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    eye_note = models.CharField(_('Note'), max_length=255, blank=True)
    ear = models.CharField(_('Ear'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    ear_note = models.CharField(_('Note'), max_length=255, blank=True)
    nose = models.CharField(_('Nose'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    nose_note = models.CharField(_('Note'), max_length=255, blank=True)
    hydration = models.CharField(_('Skin Tenting'), max_length=25, choices=DEHYDRATED_ANSWER, blank=True)
    mouth = models.CharField(_('Mouth'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    mouth_note = models.CharField(_('Note'), max_length=255, blank=True)
    mucous_membrane = models.CharField(_('Mucous Membrane'), max_length=10, choices=MUCOUS_ANSWER, blank=True)
    capillary_refill_time = models.CharField(_('Capillary Refill Time'), max_length=3, blank=True)
    superficial_lymph_nodes = models.CharField(_('Superficial Lymph Nodes'), max_length=10, choices=DEFAULT_ANSWER,
                                               blank=True)
    superficial_lymph_nodes_note = models.CharField(_('Note'), max_length=100, blank=True)
    palpable_thyroid = models.CharField(_('Palpable Thyroid'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    palpable_thyroid_note = models.CharField(_('Note'), max_length=100, blank=True)
    pulmonary_auscultation = models.CharField(_('Pulmonary Auscultation'), max_length=10, choices=DEFAULT_ANSWER,
                                              blank=True)
    pulmonary_auscultation_note = models.CharField(_('Note'), max_length=100, blank=True)
    cardiac_auscultation = models.CharField(_('Cardiac Auscultation'), max_length=10, choices=DEFAULT_ANSWER,
                                            blank=True)
    cardiac_auscultation_note = models.CharField(_('Note'), max_length=100, blank=True)
    heart_rate = models.CharField(_('Heart Rate'), max_length=10, blank=True)
    abdominal_palpation = models.CharField(_('Abdominal Palpation'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    abdominal_palpation_note = models.CharField(_('Note'), max_length=100, blank=True)
    coat = models.CharField(_('Coat'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    coat_note = models.CharField(_('Note'), max_length=100, blank=True)
    skin = models.CharField(_('Skin'), max_length=10, choices=DEFAULT_ANSWER, blank=True)
    skin_note = models.CharField(_('Note'), max_length=100, blank=True)
    musculoskeletal_system = models.CharField(_('Musculoskeletal System'), max_length=10, choices=DEFAULT_ANSWER,
                                              blank=True)
    musculoskeletal_system_note = models.CharField(_('Note'), max_length=100, blank=True)
    central_and_peripheral_nervous_system = models.CharField(_('Central and Peripheral Nervous Systems'), max_length=10,
                                                             choices=DEFAULT_ANSWER, blank=True)
    central_and_peripheral_nervous_system_note = models.CharField(_('Note'), max_length=100, blank=True)
    additional_findings = models.TextField(_('Note'), blank=True)

    # Returns the date 
    def __unicode__(self):
        return u'%s' % self.date

    def owner(self):
        return u'%s' % self.animal.owner

    # Description of the model / Sort by date
    class Meta:
        verbose_name = _('Examination')
        verbose_name_plural = _('Examinations')
        ordering = ('date', )
