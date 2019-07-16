from django import forms
from .models import Post, Album

class PostForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="No Albums Created")

    class Meta:
        model = Post
        fields = ['title', 'image', 'location', 'description', 'album']
    # def clean_title(self):
    #     album = self.cleaned_data['album']
    #     album = forms.ModelChoiceField(queryset=Album.objects.all(), empty_label="No Albums Created")

    # def user_album(self):
    #     if self.cleaned_data['name'] != self.request.user.name:
    #         raise forms.ValidationError("The name is not the same.")
    #     return self.cleaned_data['name']
    def form_valid(self, form):
        form.instance.app_user = self.request.user
        return super().form_valid(form)


class AlbumForm(forms.ModelForm):

    class Meta: 
        model = Album
        fields = ['album_title', 'album_year', 'album_description']

