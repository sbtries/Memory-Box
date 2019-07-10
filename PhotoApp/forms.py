from django import forms
from .models import Post, Album

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'location', 'description', ]

class AlbumForm(forms.ModelForm):
    class Meta: 
        model = Album
        fields = ['title', 'year', 'description']
