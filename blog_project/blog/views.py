from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    model=Blog
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5