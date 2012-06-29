# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from models import Event

class EventSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Event.public_objects.all()

    def lastmod(self, obj):
        return obj.mod_date