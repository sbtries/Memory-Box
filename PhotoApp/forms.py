from django import forms
from .models import Post, Album

class PostForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), 
  empty_label="No Albums Created")

    class Meta:
        model = Post
        fields = ['title', 'image', 'location', 'description', ]

class AlbumForm(forms.ModelForm):

    class Meta: 
        model = Album
        fields = ['album_title', 'album_year', 'album_description']
