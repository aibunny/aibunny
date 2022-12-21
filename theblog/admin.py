from django.contrib import admin
from .models import Post,Category,Comment
from .forms import BlogAdminForm
#############################################################
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Category)


#############################################################

