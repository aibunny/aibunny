

from django.contrib import admin
from django.urls import path, include 
from django.contrib.sitemaps import views

from . sitemaps import ArticleSitemap

sitemaps = {
    ArticleSitemap.name: ArticleSitemap
}


urlpatterns = [
    
    path("admin/", admin.site.urls),
    path('',include('theblog.urls')),
    path("ckeditor/",include('ckeditor_uploader.urls')),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps},name='sitemap-index'),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    
]
