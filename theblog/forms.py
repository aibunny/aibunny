from .models import Post
from  django import forms

class BlogAdminForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs= {'id': 'richtext_field'}))
    class Meta:
        model = Post
        fields = "__all__"        
       
