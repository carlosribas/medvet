from django import forms
from django.forms import DateInput, Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _

from models import Examination


class ExaminationForm(forms.ModelForm):

    class Meta:
        model = Examination

        exclude = ['animal']

        widgets = {
            'examination_type': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                     'data-error': _('This field must be filled.')},),
            'temperature': TextInput(attrs={'class': 'form-control'}),
            'bodyweight': TextInput(attrs={'class': 'form-control'}),
            'body_condition': Select(attrs={'class': 'form-control'}),
            'hydration': Select(attrs={'class': 'form-control'}),
            'mucous_membrane': Select(attrs={'class': 'form-control'}),
            'palpable_thyroid': Select(attrs={'class': 'form-control'}),
            'palpable_thyroid_note': TextInput(attrs={'class': 'form-control'}),
            'auscultation': Select(attrs={'class': 'form-control'}),
            'auscultation_note': TextInput(attrs={'class': 'form-control'}),
            'abdominal_palpation': Select(attrs={'class': 'form-control'}),
            'abdominal_palpation_note': TextInput(attrs={'class': 'form-control'}),
            'additional_findings': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
