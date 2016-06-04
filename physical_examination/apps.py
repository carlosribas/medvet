# physical_examination/apps.py

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PhysicalExaminationConfig(AppConfig):
    name = 'physical_examination'
    verbose_name = _('Physical Examination')
