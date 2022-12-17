from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,DeleteView,UpdateView
from .models import Post
from  .forms import PostForm
from django.urls import reverse_lazy
from . filters import PostFilter
from django_filters.views import FilterView
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
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update_post.html"
    #fields =['tittle','tittle_tag','body',] 
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("guess")    
    

def CategoryView(request):
   listings = Post.objects.all()
   listings_filter = PostFilter(request.GET, queryset=listings)
   context = {
       "listings_filter": listings_filter,
   }
   return render(request,"home.html",context)