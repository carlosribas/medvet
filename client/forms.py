# -*- coding: utf-8 -*-
from django import forms
from django.forms import Select, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
from client.models import Client


STATES = (('', ''), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
          ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
          ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'),
          ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
          ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
          ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'))


class ClientForm(forms.ModelForm):

    def __init__(self, data=None, *args, **kwargs):
        super(ClientForm, self).__init__(data, *args, **kwargs)
        self.fields['zipcode'].widget.attrs['onBlur'] = 'pesquisacep(this.value);'

    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': "",
                                     'data-error': _('This field must be filled.')}),
            'rg': TextInput(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={
                'class': 'form-control', 'type': 'email', 'data-error': _('Incorrect e-mail'),
                'pattern': '^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$'}),
            'phone': TextInput(attrs={'class': 'form-control telephone_number', 'pattern': '^[- ()0-9]+'}),
            'cellphone': TextInput(attrs={'class': 'form-control telephone_number', 'pattern': '^[- ()0-9]+'}),
            'zipcode': TextInput(attrs={'class': 'form-control'}),
            'street': TextInput(attrs={'class': 'form-control'}),
            'street_complement': TextInput(attrs={'class': 'form-control'}),
            'number': TextInput(attrs={'class': 'form-control'}),
            'district': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        }


class ClientAdminForm(forms.ModelForm):

    def __init__(self, data=None, *args, **kwargs):
        super(ClientAdminForm, self).__init__(data, *args, **kwargs)
        self.fields['zipcode'].widget.attrs['onBlur'] = 'pesquisacep(this.value);'

    class Meta:
        model = Client

        fields = ['state']

        widgets = {
            'state': Select(choices=STATES),
        }

    class Media:
        js = ('client/js/cep.js',)
