# -*- coding: utf-8 -*-
from django.apps import apps
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.test.client import RequestFactory

from home.views import home, report
from home.apps import HomeConfig

USER_USERNAME = 'user'
USER_PWD = 'mypassword'
USER_EMAIL = 'user@example.com'


class HomeTest(TestCase):
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

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_report_view_status_code(self):
        url = reverse('report')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reports.html')

    def test_report_url_resolves_report_view(self):
        view = resolve('/report/')
        self.assertEquals(view.func, report)


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(HomeConfig.name, 'home')
        self.assertEqual(apps.get_app_config('home').name, 'home')
