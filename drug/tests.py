# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.test import TestCase

from drug.apps import DrugConfig


class AppTest(TestCase):
    def test_apps(self):
        self.assertEqual(DrugConfig.name, 'drug')
        self.assertEqual(apps.get_app_config('drug').name, 'drug')
