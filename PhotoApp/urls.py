from django.urls import path 

from .views import DashboardView, HomePageView, CreatePostView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('', HomePageView.as_view(), name= 'home'),
    path('upload/', CreatePostView.as_view(), name='uploadpage')
]