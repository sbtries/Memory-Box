from django.shortcuts import render, redirect 

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

class DashboardView(ListView):
    model = Post
    template_name = 'pages/dashboard.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/uploadpage.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.app_user = self.request.user
        return super().form_valid(form)


#add method that saves user to the database

