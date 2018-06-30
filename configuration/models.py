# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel


class Image(SingletonModel):
    """
    Images registration will be done via Django Admin.
    """
    logo = models.FileField(_('Logo'), upload_to='images/logo/')
    background_image = models.FileField(_('Background image'), upload_to='images/background/')

    class Meta:
        verbose_name = _('Image')


class Document(SingletonModel):
    """
    Document information will be recorded through Django Admin.
    """
    footer = models.TextField(_('Footer'),
                              help_text=_('This info will be used in the footer from a document that will be printed.'))

    class Meta:
        verbose_name = _('Document')
