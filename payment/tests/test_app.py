from django.apps import apps
from django.test import TestCase
from payment.apps import PaymentConfig


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PaymentConfig.name, 'payment')
        self.assertEqual(apps.get_app_config('payment').name, 'payment')
