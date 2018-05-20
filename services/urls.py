from services import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_animal$', views.select_animal, name='select_animal'),
    url(r'^consultation/new/(?P<animal_id>\d+)/$', views.consultation_new, name='consultation_new'),
    url(r'^consultation/list/(?P<animal_id>\d+)/$', views.consultation_list, name='consultation_list'),
    url(r'^consultation/view/(?P<service_ptr_id>\d+)/$', views.consultation_view, name='consultation_view'),
    url(r'^consultation/edit/(?P<service_ptr_id>\d+)/$', views.consultation_update, name='consultation_update'),
]
