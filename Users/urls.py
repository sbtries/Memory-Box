from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomePageView.as_view(), name= 'home'),
]