from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^physical_examination/', include('physical_examination.urls')),
    url(r'^animal/', include('animal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)