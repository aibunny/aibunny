from django.urls import path
from .views import HomeView, ArticleDetailView,PostCategory
from django.conf import settings
from django.conf.urls.static import static
from . sitemaps import ArticleSitemap

sitemaps = {
    ArticleSitemap.name: ArticleSitemap
}

urlpatterns = [
    path('',HomeView,name='home'),
    
    path('<slug:slug>/',ArticleDetailView.as_view(),name='article-detail'),
    path('post/category/<int:pk>',PostCategory.as_view(),name='category'),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},
         name='sitemap-index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
     ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)