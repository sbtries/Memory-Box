from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'uploaded_at', 'description',)
