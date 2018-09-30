# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django.test import TestCase

from configuration.apps import ConfigurationConfig


class ReportsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ConfigurationConfig.name, 'configuration')
        self.assertEqual(apps.get_app_config('configuration').name, 'configuration')
