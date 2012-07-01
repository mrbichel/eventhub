from django import template
from events.models import Category

register = template.Library()

@register.assignment_tag
def get_event_categories():
    
    cats = Category.objects.filter(featured=True)
    
    return cats