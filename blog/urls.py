from django.urls import path

from .views import (
    home,
    blog_detail,
    blog_of_category,
    category,
    blog_of_tags,
    tag_create,
    blog_create,
)

from .views_cbv import BlogListView, BlogDetailView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    # path('', home, name='home'),
    # path('blog/<int:pk>', blog_detail, name='blog_detail'),
    path('category/<slug:slug>', blog_of_category, name='blog_of_category'),
    path('tag/<slug:slug>', blog_of_tags, name='blog_of_tags'),
    path('category/', category, name='category'),
    path('tag-create/', tag_create, name='tag_create'),
    # path('blog-create/', blog_create, name='blog_create'),
]

url_for_cbv = [
    path('', BlogListView.as_view(), name='home'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog-create/', BlogCreateView.as_view(), name='blog_create'),
]

urlpatterns += url_for_cbv
