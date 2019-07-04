from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

from .models import CustomUser


class HomePageView(CreateView):
    model = CustomUser
    template_name = 'pages/home.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dashboard')
