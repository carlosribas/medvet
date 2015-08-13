# -*- coding: utf-8 -*-
from django import forms
from cep.widgets import CEPInput
from django.forms import Select
from django.utils.translation import ugettext_lazy as _
from client.models import Client

STATES = (('', ''), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
          ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'),
          ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'),
          ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
          ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'),
          ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'))


class ClientAdminForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = ['zipcode', 'street', 'district', 'city', 'state']

        widgets = {
            'zipcode': CEPInput(address={'street': 'id_street', 'district': 'id_district', 'city': 'id_city',
                                         'state': 'id_state'},
                                attrs={'pattern': '\d{5}-?\d{3}', 'placeholder': _('eg. 99999-999')}),
            'state': Select(choices=STATES),
        }