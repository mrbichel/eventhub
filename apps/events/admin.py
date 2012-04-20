# -*- coding: utf-8 -*-

from django.contrib import admin
from events.models import Event, Category, TaggedEvent
from taggit.models import Tag

admin.site.unregister(Tag)

class EventAdmin(admin.ModelAdmin):
    list_display  = ('title', 'start', 'status', 'pub_date')
    list_filter   = ('pub_date', 'start', 'status')
    search_fields = ('title', 'subtitle', 'body')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'subtitle', 'start', 'end', 'location', 'body', 'english_summary', 'categories', 'image')
        }),
        
        ('Publication', {
           'fields': ('pub_date', 'status', 'featured'),
           'classes': ('collapse',)
        }),
    )

admin.site.register(Event, EventAdmin)

class TaggedEventInline(admin.StackedInline):
    model = TaggedEvent

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        TaggedEventInline
    ]

admin.site.register(Category, CategoryAdmin)