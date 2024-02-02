from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-id']

class PostDetails(DetailView):
    model = Post
    template_name = 'blog/blog.html'
class CreatePost(LoginRequiredMixin, CreateView):
     model = Post
     fields = ['title','content']
     success_url = '/'
     template_name = 'blog/newPost.html'
     def form_valid(self,form):
          form.instance.author = self.request.user
          return super().form_valid(form)
     
class DeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
     model = Post
     template_name = 'blog/deleteview.html'
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False
     success_url = '/'
class UpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     model = Post
     fields = ["title", "content"]
     template_name = 'blog/newPost.html'
     def form_valid(self, form) :
          form.instance.author = self.request.user
          return super().form_valid(form)
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.author:
               return True
          return False
     success_url = '/'


    