from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
         return self.name
    
    def get_absolute_url(self):
        return reverse('category', args=str((self.pk)))
        

class Post(models.Model):
    
        
    tittle = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
   

    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=None)
    post_date = models.DateField(auto_now_add = True)
    description = RichTextUploadingField(max_length=500)
    body = RichTextUploadingField()
    slug = AutoSlugField(populate_from=['title'])
    #read_time = models.DateTimeField(null=True, blank=True)
    
    def slugify_function(self, content):
        return content.replace('_', '-').lower()
    
    
    def __str__(self):
         return self.tittle + "|" + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=str((self.pk)))
        return reverse('home')
    


    
