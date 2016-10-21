from physical_examination import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_animal$', views.select_animal, name='select_animal'),
    url(r'^new/(?P<animal_id>\d+)/$', views.new_physical_examination, name='new_physical_examination'),
    # url(r'^view/(?P<animal_id>\d+)/$', views.animal_view, name='animal_view'),
    # url(r'^edit/(?P<animal_id>\d+)/$', views.animal_update, name='animal_edit'),
]
