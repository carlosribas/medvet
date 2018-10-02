# -*- coding: utf-8 -*-
from django.forms import EmailInput, TextInput, PasswordInput, CharField, ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import PasswordResetForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control'})

    def clean_password(self):
        return make_password(self.cleaned_data['password'])

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email, is_active=True).exclude(id=self.instance.id).count():
            raise ValidationError(_('Email already registered'))
        return email


class UserFormUpdate(UserForm):
    password = CharField(required=False,
                         widget=PasswordInput(attrs={'id': 'id_new_password1', 'class': 'form-control',
                                                     'placeholder': _('Type password'),
                                                     'onkeyup': "passwordForce(); "
                                                                "if(beginCheckPassword1) checkPassExt();"}))

    def clean_password(self):
        if self.cleaned_data['password']:
            return make_password(self.cleaned_data['password'])
        else:
            return self.instance.password


class CustomPasswordResetForm(PasswordResetForm):

    def is_valid(self):

        if not super(CustomPasswordResetForm, self).is_valid():
            return False

        # get_users returns a generator object
        users = self.get_users(self.cleaned_data['email'])

        try:
            # trying to get the first element from the generator object using __next__() once
            users.__next__()
            return True
        except StopIteration:
            self.add_error('email', _('E-mail is not registered'))
            self.add_error(None, _('E-mail is not registered'))
            return False
