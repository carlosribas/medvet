from payment import views
from django.conf.urls import url


urlpatterns = [
    url(r'^unpaid', views.unpaid, name='unpaid'),
    url(r'^services/(?P<service_list>[0-9-]+)$', views.payment_new, name='payment_new'),
    url(r'^view/(?P<payment_id>\d+)/$', views.payment_view, name='payment_view'),
    url(r'^edit/(?P<payment_id>\d+)/$', views.payment_edit, name='payment_edit'),
]
