from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime


class Examination(models.Model):
    """
    An instance of this class is an examination of an animal.

    '__unicode__'		Returns the date.
    'class Meta'		Sets the description model (singular and plural) and define ordering of data by date.
    """

    owner = models.ForeignKey('client.Client', verbose_name=_('Owner'))
    animal = models.ForeignKey('animal.Animal', verbose_name=_("Animal's Name"))
    date = models.DateField(_('Date'), default=datetime.date.today)
    temperature = models.CharField(_('Temperature'), max_length=3, blank=True, null=True)
    pulse = models.NullBooleanField(_('Pulse'), blank=True, null=True)
    pulse_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    respiratory_rate = models.CharField(_('Respiratory Rate'), max_length=10, blank=True, null=True)
    bodyweight = models.CharField(_('Bodyweight'), max_length=10, blank=True, null=True)
    body_condition = models.CharField(_('Body Condition Score'), max_length=1, blank=True, null=True)
    attitude = models.CharField(_('Attitude'), max_length=1, blank=True, null=True)
    attitude_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    face = models.CharField(_('Face'), max_length=1, blank=True, null=True)
    face_note = models.TextField(_('Note'), blank=True, null=True)
    eye = models.NullBooleanField(_('Eyes'), blank=True, null=True)
    eye_note = models.TextField(_('Note'), blank=True, null=True)
    ear = models.NullBooleanField(_('Ears'), blank=True, null=True)
    ear_note = models.TextField(_('Note'), blank=True, null=True)
    nose = models.NullBooleanField(_('Nose'), blank=True, null=True)
    nose_note = models.TextField(_('Note'), blank=True, null=True)
    hydration = models.CharField(_('Skin Tenting'), max_length=1, blank=True, null=True)
    mouth = models.NullBooleanField(_('Mouth'), blank=True, null=True)
    mouth_note = models.TextField(_('Note'), blank=True, null=True)
    mucous_membrane = models.CharField(_('Mucous Membrane'), max_length=1, blank=True, null=True)
    capillary_refill_time = models.CharField(_('Capillary Refill Time'), max_length=3, blank=True, null=True)
    superficial_lymph_nodes = models.NullBooleanField(_('Superficial Lymph Nodes'), blank=True, null=True)
    superficial_lymph_nodes_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    palpable_thyroid = models.NullBooleanField(_('Palpable Thyroid'), blank=True, null=True)
    palpable_thyroid_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    pulmonary_auscultation = models.NullBooleanField(_('Pulmonary Auscultation'), blank=True, null=True)
    pulmonary_auscultation_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    cardiac_auscultation = models.NullBooleanField(_('Cardiac Auscultation'), blank=True, null=True)
    cardiac_auscultation_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    heart_rate = models.CharField(_('Heart Rate'), max_length=10, blank=True, null=True)
    abdominal_palpation = models.NullBooleanField(_('Abdominal Palpation'), blank=True, null=True)
    abdominal_palpation_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    coat = models.NullBooleanField(_('Coat'), blank=True, null=True)
    coat_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    skin = models.NullBooleanField(_('Skin'), blank=True, null=True)
    skin_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    musculoskeletal_system = models.NullBooleanField(_('Musculoskeletal System'), blank=True, null=True)
    musculoskeletal_system_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    central_and_peripheral_nervous_system = models.NullBooleanField(_('Central and Peripheral Nervous Systems'),
                                                                    blank=True, null=True)
    central_and_peripheral_nervous_system_note = models.CharField(_('Note'), max_length=100, blank=True, null=True)
    additional_findings = models.TextField(_('Note'), blank=True, null=True)

    # Returns the date 
    def __unicode__(self):
        return u'%s' % self.date

    # Description of the model / Sort by date
    class Meta:
        verbose_name = _('Examination')
        verbose_name_plural = _('Examinations')
        ordering = ('date', )
