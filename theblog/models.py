from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor_uploader.fields import  RichTextUploadingField
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

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
    description = RichTextUploadingField(max_length=300)
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

class Project(models.Model):
    images = RichTextUploadingField()
    tittle = RichTextUploadingField()
    description = RichTextUploadingField()
    date = models.DateField(auto_now_add=True)
    git_url = models.URLField()
    web_url = models.URLField(blank=True)
    kaggle_url = models.URLField(blank=True)
    category = models.ForeignKey(Category,on_delete = models.PROTECT)
    
    def __str__(self):
        return self.tittle
    def save(self, *args, **kwargs):
        if not self.pk:  # if creating a new instance
            self.web_url = self.git_url
            self.kaggle_url = self.git_url
        super().save(*args, **kwargs)
        
        
class Skill(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name
    
class PresentDateField(models.DateField):
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        if value == timezone.localdate():
            return 'Present'
        return super().value_to_string(obj)
class Work_history(models.Model):
    start = models.DateField(null=True, blank=True)
    end = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=100)
    Description = RichTextUploadingField()
    company = models.CharField(max_length=100)
    created_at_date = models.DateField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)
    
    def save(self, *args, **kwargs):
        if self.end is None:
            self.end = 'Present'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.company}"

        
    