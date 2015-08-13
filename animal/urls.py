from django.conf.urls import *

urlpatterns = patterns('animal.views',
    (r'select_specie$', 'select_specie'),
)