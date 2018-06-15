# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.test.client import RequestFactory

from views import *
from models import Client

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

        self.factory = RequestFactory()

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

        Client.objects.create(name='Fulano de Tal')

    def test_client_new_status_code(self):
        url = reverse('client_new')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_client_new_url_resolves_client_new_view(self):
        view = resolve('/client/new')
        self.assertEquals(view.func, client_new)

    def test_client_view_status_code(self):
        client = Client.objects.first()
        url = reverse('client_view', args=(client.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_client_view_url_resolves_client_view_view(self):
        view = resolve('/client/view/1/')
        self.assertEquals(view.func, client_view)

    def test_client_update_status_code(self):
        client = Client.objects.first()
        url = reverse('client_edit', args=(client.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_client_update_url_resolves_client_update_view(self):
        view = resolve('/client/edit/1/')
        self.assertEquals(view.func, client_update)
