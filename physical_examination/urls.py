from django.conf.urls import *

urlpatterns = patterns('physical_examination.views',
    (r'select_animal$', 'select_animal'),
)