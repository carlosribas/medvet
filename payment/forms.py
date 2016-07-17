from models import Payment
from client.models import Client
from django import forms
from django.forms import Select
from django.utils.translation import ugettext_lazy as _


class PaymentForm(forms.ModelForm):

    owner = forms.ModelChoiceField(Client.objects.all(), label=_('Owner'),
                                   widget=Select(attrs={'onchange': 'ajax_filter_animal_name(this.value);'}))

    class Meta:
        model = Payment
        fields = '__all__'

    class Media:
        js = ('physical_examination/js/filter_animal_name.js',)


class ServiceItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs['style'] = "width:100px"
