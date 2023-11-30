from django.shortcuts import render, get_object_or_404

from .models import Blog, Category


# def categories():
#     return Category.objects.all()

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        # 'categories': categories()
    }
    return render(request, 'blog/home.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        "blog": blog,
        # 'categores': categories()
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_of_category(requser, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category)

    context = {
        'category': category,
        'blogs': blogs
    }
    return render(requser, 'blog/blog_of_category.html', context)