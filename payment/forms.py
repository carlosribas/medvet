from models import *
from django import forms
from django.forms import Select
from django.utils.translation import ugettext_lazy as _


STATUS = (
    (None, _('Unknown')),
    (True, _('Paid')),
    (False, _('Not paid')),
)


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['status']
        widgets = {
            'status': Select(choices=STATUS),
        }


class ServiceItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs['style'] = "width:100px"

    class Meta:
        model = ServiceItem
        fields = '__all__'
        widgets = {
            'status': Select(choices=STATUS),
        }