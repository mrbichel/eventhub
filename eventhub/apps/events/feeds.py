# -*- coding: utf-8 -*-

from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import Feed
from models import Event

class EventFeed(Feed):
    feed_type = Atom1Feed
    description_template = 'feeds/event_description.html'
    title_template = 'feeds/event_title.html'

    title = "Events from "
    subtitle = "events about social green ..."
    link = "/"

    def item_pubdate(self, obj):
        return obj.pub_date

    def items(self):
        return Event.public_objects.order_by('-pub_date')[:12]

    def item_categories(self, obj):
        return list(obj.categories.all())
  