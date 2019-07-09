from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from PhotoApp.models import Post

from .forms import PostForm
from users.forms import CustomUserCreationForm

class DashboardView(ListView):
    model = Post
    template_name = 'pages/dashboard.html'

    def user_photos(request, user):
        user_photos = Post.objects.get(app_user=user)
        user_photos.current = request.user
        return render(request, 'pages/dashboard.html')


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

# add method that saves user to the database
