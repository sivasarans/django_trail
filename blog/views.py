# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/post'

#blog delete class function


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/post'

    def get_object(self, queryset=None):
          # Use id instead of pk
        return get_object_or_404(Post, id = self.kwargs.get("id"))