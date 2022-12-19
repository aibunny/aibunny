from django.urls import path
from .views import AdminView,HomeView, ArticleDetailView


urlpatterns = [
    path('guess/',AdminView.as_view(),name='guess'),
    path('',HomeView.as_view() ,name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
     ]