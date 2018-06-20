from django import forms
from django.forms import DateInput, Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
from animal.models import Animal


class AddAnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

        widgets = {
            'owner': Select(attrs={'class': 'form-control', 'required': "",
                                   'data-error': _('This field must be filled.')}),
            'specie': Select(attrs={'class': 'form-control', 'required': "",
                                    'onchange': 'ajax_to_filter_breed_and_color(this.value);',
                                    'data-error': _('This field must be filled.')}),
            'breed': Select(attrs={'class': 'form-control', 'required': "",
                                   'data-error': _('This field must be filled.')}),
            'color': Select(attrs={'class': 'form-control'}),
            'fur': Select(attrs={'class': 'form-control'}),
            'animal_name': TextInput(attrs={'class': 'form-control', 'required': "",
                                            'data-error': _('This field must be filled.')}),
            'birthdate': DateInput(attrs={'class': 'form-control datepicker'},),
            'sex': Select(attrs={'class': 'form-control'}),
            'spay_neuter': Select(attrs={'class': 'form-control'}),
            'spay_neuter_date': TextInput(attrs={'class': 'form-control'}),
            'microchip': TextInput(attrs={'class': 'form-control'}),
            'dead': Select(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
