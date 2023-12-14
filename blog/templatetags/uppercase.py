from django import template

from blog.models import Blog

register = template.Library()


@register.filter
def title_to_uppercase(value):
    return value.upper()


@register.filter
def count_blog(value):
    return Blog.objects.filter(category__pk=value).count()
