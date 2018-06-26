import datetime

from django import forms
from django.forms import DateInput, Select, Textarea, TextInput, SelectMultiple
from django.utils.translation import ugettext_lazy as _

from services.models import Consultation, Exam, Vaccine


class ConsultationForm(forms.ModelForm):

    class Meta:
        model = Consultation
        exclude = ['animal', 'service_type']

        widgets = {
            'consultation_type': Select(attrs={'class': 'form-control'}),
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


class VaccineForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        exclude = ['animal', 'service_type', 'vaccine_in_consultation']

        widgets = {
            'vaccine_type': Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                     'data-error': _('This field must be filled.')}, ),
            'lot': TextInput(attrs={'class': 'form-control'}),
            'booster': DateInput(attrs={'class': 'form-control future-datepicker'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }


class ExamForm(forms.ModelForm):

    date = forms.DateField(input_formats=['%d/%m/%Y'], initial=datetime.date.today(),
                           widget=forms.DateInput(attrs={'class': 'form-control datepicker'}, format='%d/%m/%Y'))

    class Meta:
        model = Exam
        exclude = ['animal', 'service_type', 'exam_in_consultation', 'exam_type']

        widgets = {
            # 'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
            #                          'data-error': _('This field must be filled.')}, ),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'exam_request': Select(attrs={'class': 'form-control'})
        }
