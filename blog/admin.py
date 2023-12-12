from django.contrib import admin

from .models import Category, Blog, Tag, Comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_deleted')

