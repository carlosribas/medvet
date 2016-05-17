from physical_examination import views
from django.conf.urls import url


urlpatterns = [
    url(r'select_animal$', views.select_animal, name='select_animal')
]
