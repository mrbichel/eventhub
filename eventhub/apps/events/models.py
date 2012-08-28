# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

import datetime
import markdown
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase
from django.conf import settings
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField

def format_html(markdownText):
    md = markdown.Markdown(
        extensions=['footnotes', 'abbr', 'tables', 'headerid'] #  
    )

    return md.convert(unicode(markdownText))

class PublicManager(models.Manager):
    """Returns published posts."""
    def get_query_set(self):
        qs = super(PublicManager, self).get_query_set()
        qs = qs.filter(status=Event.PUBLIC_STATUS, 
            pub_date__lte=datetime.datetime.now())
        return qs
        
    def future(self):
        return self.get_query_set().filter(
            end__gte=datetime.datetime.now()).order_by('start')
    
    def past(self):
        return self.get_query_set().exclude(
            end__gte=datetime.datetime.now()).order_by('-start')

class Category(TagBase):
    description = models.TextField(
            help_text="A short description about what is categorised under this tag.", 
            blank=True)
    
    featured = models.BooleanField(default=False) 
    
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategorier"
    
    @models.permalink
    def get_absolute_url(self):
        return ('events_by_category', (),
            {'slug': self.slug})


class TaggedEvent(GenericTaggedItemBase):
    tag = models.ForeignKey(Category, related_name="%(app_label)s_%(class)s_items")
    

class Organizer(models.Model):
    title = models.CharField('Titel', max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(
            help_text="A short description about what is categorised under this tag.", 
            blank=True)
    
    logo = ImageField(
        upload_to="images/orgs/",
        blank=True, null=True,
    )
    
    class Meta:
        verbose_name = "Organisator"
        verbose_name_plural = "Organisatorer"
        
    def __unicode__(self):
        return self.title
            
    @models.permalink
    def get_absolute_url(self):
        return ('events_by_organizer', (),
            {'slug': self.slug})


def content_file_name(instance, filename):
    fileName, fileExtension = os.path.splitext(filename)
    d = datetime.datetime.now()
    return '/'.join(['images', d.strftime("%Y"), d.strftime("%m"), "{}{}".format(slugify(fileName), fileExtension)])

class Event(models.Model):
    DRAFT_STATUS = 0
    PUBLIC_STATUS = 1
    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (PUBLIC_STATUS, 'Public'),
    )

    title = models.CharField('Titel', max_length=200)
    subtitle = models.CharField('Undertitel', max_length=200, blank=True)
    slug = models.SlugField(max_length=200)
    
    english_summary = models.TextField(help_text="Resume på Engelsk", blank=True)
    
    body = models.TextField("Beskrivelse", help_text="Use markdown formatting.")
    html = models.TextField(editable=False, blank=True)
    
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS)
    
    start = models.DateTimeField(default=datetime.datetime.now)
    end = models.DateTimeField("Slut", blank=True)
    
    location = models.CharField("Sted", max_length=200)
    
    add_date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    pub_date = models.DateTimeField("Offentligjordt", default=datetime.datetime.now)
    mod_date = models.DateTimeField("Sidst opdateret", default=datetime.datetime.now, editable=False)
    
    featured = models.BooleanField(default=False)
    
    image = ImageField(
        upload_to=content_file_name,
        blank=True, null=True,
    )
    
    categories = TaggableManager(blank=True, through=TaggedEvent)
    
    organizer = models.ForeignKey(Organizer, blank=True, null=True)

    objects = models.Manager()
    public_objects = PublicManager()

    class Meta:
        unique_together = ('slug', 'start')

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (),
            {'year': '%04d' % self.start.year,
             'month': '%02d' % self.start.month,
             'day': '%02d' % self.start.day,
             'slug': str(self.slug)})

    def __unicode__(self):
        return self.title

    @property
    def shortable(self):
        return '<!--more-->' in self.html

    def save(self, *args, **kwargs):
        self.mod_date = datetime.datetime.now()
        self.html = format_html(self.body)
        if not self.end:
            self.end = self.start
        super(Event, self).save(*args, **kwargs)