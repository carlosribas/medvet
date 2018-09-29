from django.apps import apps
from django.test import TestCase
from services.apps import ServicesConfig


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ServicesConfig.name, 'services')
        self.assertEqual(apps.get_app_config('services').name, 'services')
