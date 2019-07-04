from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.TextField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, )
    location = models.TextField(max_length=200, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(max_length = 200, default=None)
    app_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title

