from animal import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_specie$', views.select_specie, name='select_specie'),
    url(r'^animal_record/', views.animal_record, name='animal_record'),
]
