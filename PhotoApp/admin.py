from django.contrib import admin

from PhotoApp.models import Post, Album
from users.models import CustomUser

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'uploaded_at', 'description', 'app_user', 'album')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_title', 'album_year', 'album_description', 'app_user')

