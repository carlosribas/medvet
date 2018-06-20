from animal import views
from django.conf.urls import url


urlpatterns = [
    url(r'^search', views.animal_search, name='animal_search'),
    url(r'^select_specie$', views.select_specie_to_filter_breed_and_color, name='select_specie'),
    url(r'^new', views.animal_new, name='animal_new'),
    url(r'^view/(?P<animal_id>\d+)/$', views.animal_view, name='animal_view'),
    url(r'^edit/(?P<animal_id>\d+)/$', views.animal_update, name='animal_edit'),
]
