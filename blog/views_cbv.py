from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView

from .models import Blog
from .mixins import Base
from .forms import CommentForm, BlogForm


class BlogListView(Base, ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['test'] = "Test xabar"
        return context


# class BlogDetailView(Base, View):
#     template_name = 'blog/blog_detail.html'
#
#     def get(self, request, pk):
#         blog = self.get_object(pk)
#         form = CommentForm()
#         context = {
#             'blog': blog,
#             'form': form,
#             'categories': self.category(),
#             'tags': self.tag()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, requst, pk):
#         form = CommentForm(requst.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = self.get_object(pk)
#             comment.user = requst.user
#             comment.save()
#             return redirect('blog:blog_detail', pk)
#
#
#     def get_object(self, pk):
#         return get_object_or_404(Blog, pk=pk)

class BlogDetailView(Base, FormMixin, DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = "Blog detail page"
        context['categories'] = self.category()
        return context

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blog = self.get_object()
        comment.save()
        return super().form_valid(form)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:home')
    template_name = 'blog/blog_create.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        return super().form_valid(form)
