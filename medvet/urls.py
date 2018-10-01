from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from home.views import home, language_change, report


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='custom_user/sign_in.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='custom_user/password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='custom_user/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='custom_user/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='custom_user/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$',
        auth_views.PasswordChangeView.as_view(template_name='custom_user/password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='custom_user/password_change_done.html'),
        name='password_change_done'),

    url(r'^language/(?P<language_code>(?:(?:\w{2})|(?:\w{2}\-\w{2})))$', language_change, name='language_change'),
    url(r'^report/', report, name='report'),
    url(r'^animal/', include('animal.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^custom_user/', include('custom_user.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^service/', include('services.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
