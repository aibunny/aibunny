from django.urls import path
from .views import AdminView,HomeView, ArticleDetailView,AddPostView,UpdatePostView, DeletePostView,HomeView2


urlpatterns = [
    path('guess/',AdminView.as_view(),name='guess'),
    path('',HomeView.as_view() ,name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('new_blog',AddPostView.as_view(),name='add_post'),
    path('edit_blog/<int:pk>',UpdatePostView.as_view(), name ='update_post'),
    path('delete_blog/<int:pk>',DeletePostView.as_view(), name ='delete_post'),
    path('bootstrap',HomeView2.as_view() ,name='home2'),
    
]