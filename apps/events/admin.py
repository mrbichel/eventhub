# -*- coding: utf-8 -*-

from django.contrib import admin
from events.models import Event, Category, TaggedEvent, Organizer
from taggit.models import Tag

admin.site.unregister(Tag)

class EventAdmin(admin.ModelAdmin):
    list_display  = ('title', 'start', 'status', 'pub_date')
    list_filter   = ('pub_date', 'start', 'status')
    search_fields = ('title', 'subtitle', 'body')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': 
                (('title', 'slug'), 
                'subtitle', 
                'start', 
                'end', 
                'location', 
                'body', 
                'english_summary', 
                'organizer', 
                'categories', 
                'image')
        }),
        
        ('Publication', {
           'fields': ('pub_date', 
                'status', 
                'featured'),
           'classes': ('collapse',)
        }),
    )

class TaggedEventInline(admin.StackedInline):
    model = TaggedEvent

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        TaggedEventInline
    ]

class OrganizerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ["title"]

admin.site.register(Event, EventAdmin)        
admin.site.register(Category, CategoryAdmin)
admin.site.register(Organizer, OrganizerAdmin)