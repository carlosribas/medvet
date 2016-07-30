from django import forms
from django.forms import BooleanField, DateInput, RadioSelect, Select, TextInput
from django.utils.translation import ugettext_lazy as _
from animal.models import Animal, Specie


class AnimalAdminForm(forms.ModelForm):

    specie = forms.ModelChoiceField(Specie.objects.all(), label=_('Specie'),
                                    widget=Select(attrs={'onchange': 'ajax_filter_specie_breed(this.value);'}))

    def __init__(self, *args, **kwargs):
        super(AnimalAdminForm, self).__init__(*args, **kwargs)
        self.fields['sex'].choices = self.fields['sex'].choices[1:]
        self.fields['spay_neuter'].choices = self.fields['spay_neuter'].choices[1:]
        self.fields['fur'].choices = self.fields['fur'].choices[1:]

    class Meta:
        model = Animal

        fields = ['sex', 'spay_neuter', 'fur']

        widgets = {
            'sex': RadioSelect(),
            'spay_neuter': RadioSelect(),
            'fur': RadioSelect(),
        }

    class Media:
        js = ('animal/js/animal.js',)
        css = {
            'all': ('animal/css/customization.css',)
        }


class AddAnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = '__all__'

        widgets = {
            'owner': Select(attrs={'class': 'form-control', 'required': "", 'data-error': _('Owner must be filled.')}),
            'specie': Select(attrs={'class': 'form-control', 'required': "",
                                    'data-error': _('Specie must be filled.')}),
            'breed': Select(attrs={'class': 'form-control', 'required': "", 'data-error': _('Breed must be filled.')}),
            'color': Select(attrs={'class': 'form-control', 'required': "", 'data-error': _('Color must be filled.')}),
            'fur': BooleanField(required=False),
            'animal_name': TextInput(attrs={'class': 'form-control'}),
            'birthdate': DateInput(attrs={'class': 'form-control'},),
            'sex': BooleanField(required=False),
            'spay_neuter': BooleanField(required=False),
            'spay_neuter_date': TextInput(attrs={'class': 'form-control'}),
            'microchip': TextInput(attrs={'class': 'form-control'}),
            'dead': BooleanField(required=False),
            'note': TextInput(attrs={'class': 'form-control'}),
        }
