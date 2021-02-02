from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, UpdateView

# Create your views here.
class PostListView(ListView):
    model=Blog
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def Create_Blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
   
    else:
        form = BlogForm()

    return render(request,'blog/create_blog.html',{'form':form})

def Delete_Blog(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect("blog-home")


class Edit_Blog(UpdateView):
    model = Blog
    fields = ['title', 'content', 'date_posted']

    # blog = Blog.objects.get(id=id)
    # if request.method == "POST":
    #     form = BlogForm(request.POST, instance=blog)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('blog-home')
    # else:
    #     form = BlogForm()

    # return render(request,'blog/edit_blog.html',{'blog':blog})