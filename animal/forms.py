from django import forms
from django.forms import RadioSelect, Select
from django.utils.translation import ugettext_lazy as _
from animal.models import Animal, Specie


class AnimalAdminForm(forms.ModelForm):

    specie = forms.ModelChoiceField(Specie.objects.all(), label=_('Specie'),
                                    widget=Select(attrs={'onchange': 'ajax_filter_specie_breed(this.value);'}))

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs and kwargs['instance'] is not None:
            initial = {'specie': kwargs['instance'].breed.specie.id}
            if 'initial' in kwargs and kwargs['initial'] is not None:
                kwargs['initial'].update(initial)
            else:
                kwargs['initial'] = initial
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
        js = ('/static/js/animal.js',)
        css = {
            'all': ('/static/css/customization.css',)
        }
