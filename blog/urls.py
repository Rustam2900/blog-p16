from django.urls import path

from .views import home, blog_detail, blog_of_category

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('blog/<int:pk>', blog_detail, name='blog_detail'),
    path('category/<slug:slug>', blog_of_category, name='blog_of_category')
]