from django.contrib import admin

from .models import Category, Blog, Tag, Comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
