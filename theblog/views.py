from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post ,Category ,Project, Work_history
from hitcount.views import HitCountDetailView


# Create your views here.


def  HomeView(request):
    postList= Post.objects.all().order_by('-post_date')
    categoryList= Category.objects.all()
    
    return render(request,"home.html",{"post":postList, "category":categoryList})
    
    
    
class ArticleDetailView(HitCountDetailView):
    model = Post
    template_name = "article_details.html"
    count_hit = True
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get(self, request, *args, **kwargs):
        print(self.kwargs['slug'])
        return super().get(request, *args, **kwargs)
    
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
    
class ProjectView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'project'    
    ordering = ['-date'] 
    
def  ProjectView(request):
    projectList= Project.objects.all().order_by('-date')
    employmentList= Work_history.objects.all().order_by('-created_at_date')
    
    return render(request,"project.html",{"project":projectList, "work":employmentList})

### TO DO ##
