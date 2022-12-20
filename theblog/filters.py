import django_filters
from . models import Post

class CategoryFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Post.category)
    class Meta:
        model = Post
        fields = ['category']