from client.models import Client
from physical_examination.models import Examination
from django import forms
from django.forms import DateInput, RadioSelect, Select, TextInput
from django.utils.translation import ugettext_lazy as _


BODY_CONDITION = (
    ('0', _('1 - Very thin')),
    ('1', _('2 - Underweight')),
    ('2', _('3 - Ideal weight')),
    ('3', _('4 - Overweight')),
    ('4', _('5 - Obese')),
)

DEFAULT_ANSWER = (
    ('False', _('Normal')),
    ('True', _('Abnormal')),
)

ATTITUDE_ANSWER = (
    ('0', _('Bright and Alert')),
    ('1', _('Quiet but Alert')),
    ('2', _('Lethargic')),
    ('3', _('Dull')),
    ('4', _('Hyperactive')),
    ('5', _('Other')),
)

FACE_ANSWER = (
    ('0', _('Normal')),
    ('1', _('Head tilt')),
    ('2', _('Abnormal')),
)

DEHYDRATED_ANSWER = (
    ('0', _('No dehydration')),
    ('1', _('Less than 5% - Reports loss of liquids')),
    ('2', _('5 to 6% - Mild')),
    ('3', _('7 to 9% - Moderate')),
    ('4', _('10 to 12% - Severe')),
    ('5', _('12 to 15% - Hypovolemic shock')),
)

MUCOUS_ANSWER = (
    ('0', _('Pink')),
    ('1', _('Blue')),
    ('2', _('Pale')),
    ('3', _('Icteric')),
    ('4', _('Congested')),
)


class ExaminationAdminForm(forms.ModelForm):

    owner = forms.ModelChoiceField(Client.objects.all(), label=_('Owner'),
                                   widget=Select(attrs={'onchange': 'ajax_filter_animal_name(this.value);'}))

    class Meta:
        model = Examination

        fields = ['pulse', 'body_condition', 'attitude', 'face', 'eye', 'ear', 'nose', 'hydration', 'mouth',
                  'mucous_membrane', 'superficial_lymph_nodes', 'palpable_thyroid', 'pulmonary_auscultation',
                  'cardiac_auscultation', 'abdominal_palpation', 'coat', 'skin', 'musculoskeletal_system',
                  'central_and_peripheral_nervous_system']

        widgets = {
            'pulse': RadioSelect(choices=DEFAULT_ANSWER),
            'body_condition': RadioSelect(choices=BODY_CONDITION),
            'attitude': RadioSelect(choices=ATTITUDE_ANSWER),
            'face': RadioSelect(choices=FACE_ANSWER),
            'eye': RadioSelect(choices=DEFAULT_ANSWER),
            'ear': RadioSelect(choices=DEFAULT_ANSWER),
            'nose': RadioSelect(choices=DEFAULT_ANSWER),
            'hydration': RadioSelect(choices=DEHYDRATED_ANSWER),
            'mouth': RadioSelect(choices=DEFAULT_ANSWER),
            'mucous_membrane': RadioSelect(choices=MUCOUS_ANSWER),
            'superficial_lymph_nodes': RadioSelect(choices=DEFAULT_ANSWER),
            'palpable_thyroid': RadioSelect(choices=DEFAULT_ANSWER),
            'pulmonary_auscultation': RadioSelect(choices=DEFAULT_ANSWER),
            'cardiac_auscultation': RadioSelect(choices=DEFAULT_ANSWER),
            'abdominal_palpation': RadioSelect(choices=DEFAULT_ANSWER),
            'coat': RadioSelect(choices=DEFAULT_ANSWER),
            'skin': RadioSelect(choices=DEFAULT_ANSWER),
            'musculoskeletal_system': RadioSelect(choices=DEFAULT_ANSWER),
            'central_and_peripheral_nervous_system': RadioSelect(choices=DEFAULT_ANSWER),
        }

    class Media:
        js = ('physical_examination/js/physical_examination.js',
              'physical_examination/js/filter_animal_name.js')
        css = {
            'all': ('physical_examination/css/customization.css',)
        }


class ExaminationForm(forms.ModelForm):

    class Meta:
        model = Examination

        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={'class': 'form-control datepicker'},),
            'temperature': TextInput(attrs={'class': 'form-control'}),
            'pulse': RadioSelect(choices=DEFAULT_ANSWER),
            'pulse_note': TextInput(attrs={'class': 'form-control'}),
            'respiratory_rate': TextInput(attrs={'class': 'form-control'}),
            'bodyweight': TextInput(attrs={'class': 'form-control'}),
            'body_condition': RadioSelect(choices=BODY_CONDITION),
            'attitude': RadioSelect(choices=ATTITUDE_ANSWER),
            'attitude_note': TextInput(attrs={'class': 'form-control'}),
            'face': RadioSelect(choices=FACE_ANSWER),
            'face_note': TextInput(attrs={'class': 'form-control'}),
            'eye': RadioSelect(choices=DEFAULT_ANSWER),
            'eye_note': TextInput(attrs={'class': 'form-control'}),
            'ear': RadioSelect(choices=DEFAULT_ANSWER),
            'ear_note': TextInput(attrs={'class': 'form-control'}),
            'nose': RadioSelect(choices=DEFAULT_ANSWER),
            'nose_note': TextInput(attrs={'class': 'form-control'}),
            'hydration': RadioSelect(choices=DEHYDRATED_ANSWER),
            'mouth': RadioSelect(choices=DEFAULT_ANSWER),
            'mouth_note': TextInput(attrs={'class': 'form-control'}),
            'mucous_membrane': RadioSelect(choices=MUCOUS_ANSWER),
            'superficial_lymph_nodes': RadioSelect(choices=DEFAULT_ANSWER),
            'palpable_thyroid': RadioSelect(choices=DEFAULT_ANSWER),
            'pulmonary_auscultation': RadioSelect(choices=DEFAULT_ANSWER),
            'cardiac_auscultation': RadioSelect(choices=DEFAULT_ANSWER),
            'abdominal_palpation': RadioSelect(choices=DEFAULT_ANSWER),
            'coat': RadioSelect(choices=DEFAULT_ANSWER),
            'coat_note': TextInput(attrs={'class': 'form-control'}),
            'skin': RadioSelect(choices=DEFAULT_ANSWER),
            'skin_note': TextInput(attrs={'class': 'form-control'}),
            'musculoskeletal_system': RadioSelect(choices=DEFAULT_ANSWER),
            'musculoskeletal_system_note': TextInput(attrs={'class': 'form-control'}),
            'central_and_peripheral_nervous_system': RadioSelect(choices=DEFAULT_ANSWER),
        }