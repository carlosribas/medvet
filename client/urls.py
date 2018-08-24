from client import views
from django.conf.urls import url


urlpatterns = [
    url(r'^new', views.client_new, name='client_new'),
    url(r'^view/(?P<client_id>\d+)/$', views.client_view, name='client_view'),
    url(r'^edit/(?P<client_id>\d+)/$', views.client_update, name='client_edit'),
    url(r'^list', views.client_list, name='client_list'),
    url(r'^(?P<client_id>\d+)/services/$', views.client_service_list, name='client_service_list'),
]
