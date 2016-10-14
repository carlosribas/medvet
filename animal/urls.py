from animal import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_specie$', views.select_specie, name='select_specie'),
    url(r'^animal_record/', views.animal_record, name='animal_record'),
    url(r'^add_animal/', views.add_animal, name='add_animal'),
    url(r'^animal/(?P<animal_id>\d+)/$', views.animal_view, name='animal_view'),
    url(r'^animal/edit/(?P<animal_id>\d+)/$', views.animal_update, name='animal_edit'),
]
