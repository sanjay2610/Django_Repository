from django.urls import path
from . import views
from .views import PostListView, Create_Blog, Edit_Blog

urlpatterns=[
    path('', PostListView.as_view(), name='blog-home'),
    path('create/', Create_Blog, name='create-blog'),
    path('delete/<int:id>', views.Delete_Blog),
    path('blog/<int:pk>/update/', Edit_Blog.as_view(), name='edit-blog'),
    ]