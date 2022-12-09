from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date,timezone
from ckeditor.fields import  RichTextField
# Create your models here.



class Post(models.Model):
    tittle = models.CharField(max_length=255)
    tittle_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    
    #body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=255,default='ML')
    def __str__(self):
         return self.tittle + "|" + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=str((self.pk)))
        return reverse('home')
    

class Category(models.Model):
    name =models.CharField(max_length=255)
    def __str__(self):
         return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.tittle) #, user name self.name) 