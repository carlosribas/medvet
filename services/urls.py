from services import views
from django.conf.urls import url


urlpatterns = [
    # Consultation
    url(r'^consultation/new/(?P<animal_id>\d+)/$', views.consultation_new, name='consultation_new'),
    url(r'^consultation/list/(?P<animal_id>\d+)/$', views.consultation_list, name='consultation_list'),
    url(r'^consultation/view/(?P<service_ptr_id>\d+)/$', views.consultation_view, name='consultation_view'),
    url(r'^consultation/edit/(?P<service_ptr_id>\d+)/$', views.consultation_update, name='consultation_update'),
    url(r'^consultation/(?P<service_ptr_id>\d+)/animal/(?P<animal_id>\d+)/vaccine/new/$', views.vaccine_new,
        name='vaccine_in_consultation'),
    url(r'^consultation/(?P<service_ptr_id>\d+)/animal/(?P<animal_id>\d+)/exam/new/$', views.exam_new,
        name='exam_in_consultation'),

    # Vaccine
    url(r'^vaccine/new/(?P<animal_id>\d+)/$', views.vaccine_new, name='vaccine_new'),
    url(r'^vaccine/list/(?P<animal_id>\d+)/$', views.vaccine_list, name='vaccine_list'),
    url(r'^vaccine/view/(?P<service_ptr_id>\d+)/$', views.vaccine_view, name='vaccine_view'),
    url(r'^vaccine/edit/(?P<service_ptr_id>\d+)/$', views.vaccine_update, name='vaccine_update'),
    url(r'^vaccine/booster_list', views.vaccine_booster_list, name='vaccine_booster_list'),

    # Exam
    url(r'^exam/new/(?P<animal_id>\d+)/$', views.exam_new, name='exam_new'),
    url(r'^exam/list/(?P<animal_id>\d+)/$', views.exam_list, name='exam_list'),
    url(r'^exam/view/(?P<service_ptr_id>\d+)/$', views.exam_view, name='exam_view'),
    url(r'^exam/edit/(?P<service_ptr_id>\d+)/$', views.exam_update, name='exam_update'),
]
