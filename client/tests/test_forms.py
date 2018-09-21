# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase

from client.models import Client
from client.forms import ClientForm

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class ClientTest(TestCase):
    def setUp(self):
        """
        Configure authentication and variables to start each test
        """

        self.user = User.objects.create_user(username=USER_USERNAME, email=USER_EMAIL, password=USER_PWD)
        self.user.is_staff = True
        self.user.save()

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

    def test_valid_client_form(self):
        client = Client.objects.create(name='Carlos')
        data = {'name': client.name}
        form = ClientForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_client_form(self):
        """
        Using an invalid email
        """
        client = Client.objects.create(name='Eduardo', email='edu')
        data = {'name': client.name, 'email': client.email}
        form = ClientForm(data=data)
        self.assertFalse(form.is_valid())
