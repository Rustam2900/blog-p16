from django.shortcuts import render, get_object_or_404, redirect

from .forms import TagForm, BlogForm, CommentForm
from .models import Blog, Category, Tag


# def categories():
#     return Category.objects.all()

def home(request):
    blogs = Blog.objects.all()
    search = request.GET.get('search')
    if search is not None:
        blogs = blogs.filter(title__icontains=search)
    context = {
        'blogs': blogs,
        # 'categories': categories()
    }
    return render(request, 'blog/home.html', context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.blog = blog
        comment.user = request.user
        comment.save()
        return redirect('blog:blog_detail', blog.pk)
    else:
        form = CommentForm()
    context = {
        "blog": blog,
        "form": form,
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


def category(request):

    return render(request, 'blog/categories.html')


def blog_of_tags(requser, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Blog.objects.filter(tags=tag)

    context = {
        'tag': tag,
        'blogs': blogs
    }
    return render(requser, 'blog/blog_of_category.html', context)


def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Tag.objects.create(name=name)
            return redirect('blog:home')
        else:
            return redirect('blog:home')
    else:
        form = TagForm()

    context = {
        'form': form
    }
    return render(request, 'blog/tag_create.html', context)

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = user
            blog.save()
            return redirect('blog:blog_detail', blog.pk)
    form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'blog/blog_create.html', context)


