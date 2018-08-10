from payment import views
from django.conf.urls import url


urlpatterns = [
    url(r'^unpaid', views.unpaid, name='unpaid'),
    url(r'^new/(?P<service_id>\d+)/$', views.service_payment, name='service_payment'),
]
