from django import forms
from .models import Post, Album

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'location', 'description', 'album']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['album']
        album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="No Albums Created")

    def user_album(self):
        if self.cleaned_data['name'] != self.request.user.name:
            raise forms.ValidationError("The name is not the same.")
        return self.cleaned_data['name']
    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="No Albums Created")

class AlbumForm(forms.ModelForm):

    class Meta: 
        model = Album
        fields = ['album_title', 'album_year', 'album_description']

