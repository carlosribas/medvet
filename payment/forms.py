from django import forms
from django.forms import DateInput, Select, Textarea, NumberInput
from django.utils.translation import ugettext_lazy as _

from payment.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['service', 'total']

        widgets = {
            'payment_method': Select(attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control datepicker', 'required': "",
                                     'data-error': _('This field must be filled.')}, ),
            'discount_or_increase': NumberInput(attrs={'class': 'form-control', 'onchange': 'updateInput()'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
