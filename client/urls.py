from client import views
from django.conf.urls import url


urlpatterns = [
    url(r'^new', views.client_new, name='client_new'),
    url(r'^view/(?P<client_id>\d+)/$', views.client_view, name='client_view'),
    url(r'^edit/(?P<client_id>\d+)/$', views.client_update, name='client_edit'),
    url(r'^search', views.client_search, name='client_search'),
]
