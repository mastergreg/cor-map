from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from core.views import landing
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', landing),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                   'document_root': settings.MEDIA_ROOT, }),
    # url(r'^regnum/', include('regnum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
