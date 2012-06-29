# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, url
from events.feeds import EventFeed
from django.views.generic.simple import redirect_to

urlpatterns = patterns('events.views',

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        'detail',
        name='detail'
    ),

    url(r'^c/(?P<slug>[^/]+)/$',
        'by_category',
        name='events_by_category'
    ),
    
    url(r'^o/(?P<slug>[^/]+)/$',
        'by_organizer',
        name='events_by_organizer'
    ),
    
    url(r'^o/(?P<slug>[^/]+)/embed/$',
        'organizer_embed',
        name='organizer_embed'
    ),
    
    
    url(r'^categories/$',
        'categories',
        name='categories'
    ),
    
    
    url(r'^past/$',
        'past',
        name='past'
    ),
    
    url(r'^$',
        'index',
        name='index'
    ),

)

urlpatterns += patterns('',
    url(r'^feed/$', EventFeed(), name="feed"),
    )