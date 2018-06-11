# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from views import authentication


class AuthenticationTest(TestCase):
    def test_authentication_view_status_code(self):
        url = reverse('authentication')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_authentication_url_resolves_authentication_view(self):
        view = resolve('/')
        self.assertEquals(view.func, authentication)
