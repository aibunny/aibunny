from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    tittle = models.CharField(max_length=255)
    tittle_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,default=User.objects.get(username='madbunny'),on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
         return self.tittle + "|" + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=str((self.pk)))