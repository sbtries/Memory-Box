from django.urls import path 

from .views import CreatePostView

from . import views

urlpatterns = [
    path('upload/', CreatePostView.as_view(), name='uploadpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_photos/<slug:user>', views.user_photos, name='user_photos'),
]