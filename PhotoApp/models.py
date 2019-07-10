from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django import forms


class Post(models.Model):
    title = models.TextField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, )
    location = models.TextField(max_length=200, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length = 200, default=None)
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_app_user')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, null=True, blank=True, related_name='album_album')

    def __str__(self):
        return self.title

class Album(models.Model):
    album_title = models.CharField(max_length=250, blank=True, null=True, default=None)
    album_images = models.ManyToManyField(Post, blank=True, null=True, default=None, related_name='post_images')
    album_year = models.CharField(max_length=250, blank=True, null=True, default=None)
    album_description = models.CharField(max_length=250, blank=True, null=True, default=None)
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_album')
    
    def __str__(self):
        return self.album_title


