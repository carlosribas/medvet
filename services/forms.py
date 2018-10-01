import datetime

from django import forms
from django.forms import DateInput, Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _

from services.models import Consultation, Exam, Vaccine, VaccineType


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

    booster = forms.DateField(
        input_formats=['%d/%m/%Y'], required=False,
        widget=forms.DateInput(attrs={'class': 'form-control future-datepicker'}, format='%d/%m/%Y')
    )

    class Meta:
        model = Vaccine
        exclude = ['animal', 'service_type', 'vaccine_in_consultation']

        widgets = {
            'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                     'data-error': _('This field must be filled.')}, ),
            'lot': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }

    def __init__(self, *args, **kwargs):
        super(VaccineForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        self.fields['vaccine_type'] = forms.ModelChoiceField(
            queryset=VaccineType.objects.filter(vaccine_for=initial['specie']),
            widget=forms.Select(attrs={'class': 'form-control'})
        )


class ExamForm(forms.ModelForm):

    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'class': 'form-control datepicker'},
                               format='%d/%m/%Y'), initial=datetime.date.today()
    )
    exam_file = forms.FileField(required=False)

    class Meta:
        model = Exam
        exclude = ['animal', 'service_type', 'exam_in_consultation', 'exam_list']

        widgets = {
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'exam_type': Select(attrs={'class': 'form-control'})
        }
