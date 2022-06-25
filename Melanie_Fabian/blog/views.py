from attr import fields
from django.shortcuts import render
from django.views.generic.list import ListView

from blog.models import Post

class PostListView(ListView):
    model = Post

class PostCreateView(ListView):
    model = Post
    fields = "__all__"
    sucess_url = reverse_lazy("blog:all")

class PostDetailView(ListView):
    model = Post

class PostUpdateView(ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(ListView):
    model=Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")

# Create your views here.
