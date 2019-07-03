from django.urls import path 

from .views import DashboardView, CreatePostView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('upload/', CreatePostView.as_view(), name='uploadpage')
]