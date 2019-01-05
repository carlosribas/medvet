# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.test import TestCase

from medicine.apps import MedicineConfig


class AppTest(TestCase):
    def test_apps(self):
        self.assertEqual(MedicineConfig.name, 'medicine')
        self.assertEqual(apps.get_app_config('medicine').name, 'medicine')
