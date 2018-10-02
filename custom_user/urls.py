from django.conf.urls import url

from custom_user import views


urlpatterns = [
    url(r'^search', views.user_list, name='user_list'),
    url(r'^new/$', views.new_user, name='new_user'),
    url(r'^edit/(?P<user_id>\d+)/$', views.update_user, name='update_user'),
]
