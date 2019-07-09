from django.shortcuts import render, redirect 

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

class DashboardView(ListView):
    model = Post
    template_name = 'pages/dashboard.html'

    def user_info(self, form):
        form.instance.app_user = self.request.user
        return super().user_info(form)

    # def user_photos(self, request):
    #     user = Post.objects.get(id=app_user)
    #     user.current_user = request.user
    #     print('hello!')
    #     return super().user_photos()

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/uploadpage.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.app_user = self.request.user
        return super().form_valid(form)

#add method that saves user to the database

