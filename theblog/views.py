from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post ,Category
from hitcount.views import HitCountDetailView


# Create your views here.

class AdminView(ListView):
    model= Post
    template_name="admin.html"
    
class HomeView(ListView):
    model= Post
    template_name="home.html"
    ordering = ['-post_date']
    
    
    
class ArticleDetailView(HitCountDetailView):
    model = Post
    template_name = "article_details.html"
    count_hit = True
    
class PostCategory(ListView):
    model = Post
    template_name = "category.html"
    def get_queryset(self):
        self.category = get_object_or_404(Category,pk=self.kwargs['pk']) 
        return Post.objects.filter(category=self.category)
    
    def get_context_data(self,**kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
    

def category(request):
    categories = Category.objects.all()
    context =  {'categories': categories}
    return render (request, 'home.html', context)