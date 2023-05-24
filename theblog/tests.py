from django.test import TestCase
from django.contrib.auth.models import User

from . models import Post 
# Create your tests here.

class PostTestCase(TestCase):
    def test_create_post(self):
        user  = User.objects.create(email = 'johndoe@gmail.com',first_name = 'John',last_name = 'Doe')
        user.set_password('password12!')
        user.save()
        post = Post.objects.create(tittle='CNN', author= user)
        post.save()
        
        
        self.assertEqual(str(post), "CNN|")

