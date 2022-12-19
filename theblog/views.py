from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,DeleteView,UpdateView
from .models import Post
from  .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

class AdminView(ListView):
    model= Post
    template_name="admin.html"
    
class HomeView(ListView):
    model= Post
    template_name="home.html"
    ordering = ['-post_date']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"
    
