from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


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
    description = RichTextUploadingField(max_length=160)
    body = RichTextUploadingField()
    slug = models.SlugField(max_length=50,editable=False, unique=True)
    
    

    
    
  
    def __str_(self):
        return self.slug
    
    def __str__(self):
         return self.tittle + "|" + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=str((self.pk)))
        return reverse('home')
    

    
@receiver(pre_save, sender=Post)
def create_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.tittle)
    
pre_save.connect(create_slug, sender=Post)
