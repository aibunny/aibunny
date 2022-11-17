from tkinter.tix import Select

from django.forms import ChoiceField
from .models import Post,Category
from  django import forms
Choices = Category.objects.all().values_list('name','name')

choice_list= []
for item in Choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('tittle','tittle_tag','body','category','author')
        
        widgets = {
            'tittle': forms.TextInput( attrs= {'class':'form-control'}),
            'tittle_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(choices  =choice_list, attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            
             
        }  