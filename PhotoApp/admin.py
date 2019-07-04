from django.contrib import admin

from PhotoApp.models import Post
from users.models import CustomUser

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'uploaded_at', 'description', 'app_user')


