from payment import views
from django.conf.urls import url


urlpatterns = [
    url(r'^unpaid', views.unpaid, name='unpaid'),
    url(r'^services/(?P<service_list>[0-9-]+)$', views.client_payment, name='client_payment'),
]
