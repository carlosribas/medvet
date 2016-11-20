from django import forms
from django.forms import DateInput, Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _

from models import Examination


class ExaminationForm(forms.ModelForm):

    class Meta:
        model = Examination

        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                     'data-error': _('This field must be filled.')},),
            'temperature': TextInput(attrs={'class': 'form-control'}),
            'pulse': Select(attrs={'class': 'form-control'}),
            'pulse_note': TextInput(attrs={'class': 'form-control'}),
            'respiratory_rate': TextInput(attrs={'class': 'form-control'}),
            'heart_rate': TextInput(attrs={'class': 'form-control'}),
            'bodyweight': TextInput(attrs={'class': 'form-control'}),
            'body_condition': Select(attrs={'class': 'form-control'}),
            'attitude': Select(attrs={'class': 'form-control'}),
            'attitude_note': TextInput(attrs={'class': 'form-control'}),
            'face': Select(attrs={'class': 'form-control'}),
            'face_note': TextInput(attrs={'class': 'form-control'}),
            'eye': Select(attrs={'class': 'form-control'}),
            'eye_note': TextInput(attrs={'class': 'form-control'}),
            'ear': Select(attrs={'class': 'form-control'}),
            'ear_note': TextInput(attrs={'class': 'form-control'}),
            'nose': Select(attrs={'class': 'form-control'}),
            'nose_note': TextInput(attrs={'class': 'form-control'}),
            'hydration': Select(attrs={'class': 'form-control'}),
            'mouth': Select(attrs={'class': 'form-control'}),
            'mouth_note': TextInput(attrs={'class': 'form-control'}),
            'mucous_membrane': Select(attrs={'class': 'form-control'}),
            'capillary_refill_time': TextInput(attrs={'class': 'form-control'}),
            'superficial_lymph_nodes': Select(attrs={'class': 'form-control'}),
            'superficial_lymph_nodes_note': TextInput(attrs={'class': 'form-control'}),
            'palpable_thyroid': Select(attrs={'class': 'form-control'}),
            'palpable_thyroid_note': TextInput(attrs={'class': 'form-control'}),
            'pulmonary_auscultation': Select(attrs={'class': 'form-control'}),
            'pulmonary_auscultation_note': TextInput(attrs={'class': 'form-control'}),
            'cardiac_auscultation': Select(attrs={'class': 'form-control'}),
            'cardiac_auscultation_note': TextInput(attrs={'class': 'form-control'}),
            'abdominal_palpation': Select(attrs={'class': 'form-control'}),
            'abdominal_palpation_note': TextInput(attrs={'class': 'form-control'}),
            'coat': Select(attrs={'class': 'form-control'}),
            'coat_note': TextInput(attrs={'class': 'form-control'}),
            'skin': Select(attrs={'class': 'form-control'}),
            'skin_note': TextInput(attrs={'class': 'form-control'}),
            'musculoskeletal_system': Select(attrs={'class': 'form-control'}),
            'musculoskeletal_system_note': TextInput(attrs={'class': 'form-control'}),
            'central_and_peripheral_nervous_system': Select(attrs={'class': 'form-control'}),
            'additional_findings': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
