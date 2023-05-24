from django.urls import path
from .views import HomeView, ArticleDetailView,PostCategory,ProjectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView,name='home'),    
    path('<slug:slug>/',ArticleDetailView.as_view(),name='article-detail'),
    path('post/category/<int:pk>',PostCategory.as_view(),name='category'),
    path('portfolio',ProjectView, name='portfolio'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)