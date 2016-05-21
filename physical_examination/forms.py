from django import forms
from django.forms import RadioSelect, Select
from django.utils.translation import ugettext_lazy as _
from physical_examination.models import Examination

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

    class Meta:
        model = Examination

        fields = ['pulse', 'body_condition', 'attitude', 'face', 'eye', 'ear', 'nose', 'hydration', 'mouth',
                  'mucous_membrane', 'superficial_lymph_nodes', 'palpable_thyroid', 'pulmonary_auscultation',
                  'cardiac_auscultation', 'abdominal_palpation', 'coat', 'skin', 'musculoskeletal_system',
                  'central_and_peripheral_nervous_system', 'owner']

        widgets = {
            'owner': Select(attrs={'onchange': 'ajax_filter_animal_name(this.value);'}),
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
        js = ('/static/js/physical_examination.js',)
        css = {
            'all': ('/static/css/customization.css',)
        }
