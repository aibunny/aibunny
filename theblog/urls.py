from django.urls import path
from .views import HomeView, ArticleDetailView,PostCategory,PostAndCatView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',PostAndCatView,name='home'),
    
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('post/category/<int:pk>',PostCategory.as_view(),name='category'),
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)