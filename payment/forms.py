from django import forms
from django.forms import DateInput, Select, Textarea, NumberInput
from django.utils.translation import ugettext_lazy as _

from payment.models import Payment


class PaymentForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y'], required=True, widget=forms.DateInput(
            attrs={'class': 'form-control datepicker', 'data-error': _('This field must be filled.')},
            format='%d/%m/%Y')
    )

    class Meta:
        model = Payment
        exclude = ['service', 'total']

        widgets = {
            'payment_method': Select(attrs={'class': 'form-control'}),
            'discount_or_increase': NumberInput(attrs={'class': 'form-control', 'onchange': 'updateInput()'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }
