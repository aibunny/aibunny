from tkinter.tix import Select

from django.forms import ChoiceField
from .models import Post
from  django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('tittle','body','category','author')
        
        widgets = {
            'tittle': forms.TextInput( attrs= {'class':'form-control'}),
            'category': forms.Select(attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            
             
        }  

class CategoryFilterForm(forms.Form):
    category = forms.CharField()