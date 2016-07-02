from client.models import Client
from models import RequestForExamination
from django import forms
from django.forms import CheckboxSelectMultiple, Select
from django.utils.translation import ugettext_lazy as _


# class ResultForm(forms.ModelForm):
#
#     owner = forms.ModelChoiceField(Client.objects.all(), label=_('Owner'),
#                                    widget=Select(attrs={'onchange': 'ajax_filter_animal_name(this.value);'}))
#
#     class Meta:
#         model = Result
#         fields = '__all__'
#
#
class RequestForExaminationForm(forms.ModelForm):

    owner = forms.ModelChoiceField(Client.objects.all(), label=_('Owner'),
                                   widget=Select(attrs={'onchange': 'ajax_filter_animal_name(this.value);'}))

    def __init__(self, *args, **kwargs):
        super(RequestForExaminationForm, self).__init__(*args, **kwargs)
        self.fields['parasitological_exam'].empty_label = None
        self.fields['hematology_exam'].empty_label = None
        self.fields['renal_profile_exam'].empty_label = None
        self.fields['hepatic_profile_exam'].empty_label = None
        self.fields['proteins_exam'].empty_label = None
        self.fields['endocrinology_exam'].empty_label = None
        self.fields['electrolytes_exam'].empty_label = None
        self.fields['microbiology_exam'].empty_label = None
        self.fields['anatomopathology_exam'].empty_label = None
        self.fields['image_exam'].empty_label = None
        self.fields['other_exam'].empty_label = None

    class Meta:
        model = RequestForExamination

        fields = ['parasitological_exam', 'hematology_exam', 'renal_profile_exam', 'hepatic_profile_exam',
                  'proteins_exam', 'endocrinology_exam', 'electrolytes_exam', 'microbiology_exam',
                  'anatomopathology_exam', 'image_exam', 'other_exam']

        widgets = {
            'parasitological_exam': CheckboxSelectMultiple(),
            'hematology_exam': CheckboxSelectMultiple(),
            'renal_profile_exam': CheckboxSelectMultiple(),
            'hepatic_profile_exam': CheckboxSelectMultiple(),
            'proteins_exam': CheckboxSelectMultiple(),
            'endocrinology_exam': CheckboxSelectMultiple(),
            'electrolytes_exam': CheckboxSelectMultiple(),
            'microbiology_exam': CheckboxSelectMultiple(),
            'anatomopathology_exam': CheckboxSelectMultiple(),
            'image_exam': CheckboxSelectMultiple(),
            'other_exam': CheckboxSelectMultiple(),
        }

    class Media:
        js = ('physical_examination/js/filter_animal_name.js',)
        css = {
            'all': ('examination/css/customization.css',)
        }
