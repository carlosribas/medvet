from animal import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_specie$', views.select_specie, name='select_specie'),
    url(r'^new', views.animal_new, name='animal_new'),
    url(r'^view/(?P<animal_id>\d+)/$', views.animal_view, name='animal_view'),
    url(r'^edit/(?P<animal_id>\d+)/$', views.animal_update, name='animal_edit'),
]
