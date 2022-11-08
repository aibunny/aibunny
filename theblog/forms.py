from tkinter.tix import Select
from .models import Post
from  django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('tittle','tittle_tag','body','author')
        
        widgets = {
            'tittle': forms.TextInput( attrs= {'class':'form-control'}),
            'tittle_tag': forms.TextInput(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
            
             
        } 