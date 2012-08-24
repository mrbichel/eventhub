from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap
from events.sitemap import EventSitemap
from django.conf import settings

admin.autodiscover()

sitemaps = {
    'pages': FlatPageSitemap,
    'events': EventSitemap,
}

urlpatterns = patterns('',
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),

    url(r'^grappelli/', include('grappelli.urls')),
    
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    url(r'^', include('events.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)