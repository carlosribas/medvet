from payment import views
from django.conf.urls import url


urlpatterns = [
    url(r'^unpaid', views.unpaid, name='unpaid'),
]
