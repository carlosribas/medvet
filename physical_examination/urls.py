from physical_examination import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_animal$', views.select_animal, name='select_animal'),
    url(r'^new/(?P<animal_id>\d+)/$', views.physical_examination_new, name='new_physical_examination'),
    url(r'^list/(?P<animal_id>\d+)/$', views.physical_examination_list, name='physical_examination_list'),
    url(r'^view/(?P<physical_examination_id>\d+)/$', views.physical_examination_view, name='physical_examination_view'),
    url(r'^edit/(?P<physical_examination_id>\d+)/$', views.physical_examination_update,
        name='physical_examination_update'),
]
