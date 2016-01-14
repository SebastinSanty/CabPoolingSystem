from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'homepro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'sample.views.contact', name='contact'),
    url(r'^about/$', 'sample.views.contact', name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

 
 ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
	
