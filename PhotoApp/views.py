from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from PhotoApp.models import Post, Album

from .forms import PostForm, AlbumForm
from users.forms import CustomUserCreationForm

class DashboardView(ListView):
    model = Album
    template_name = 'pages/dashboard.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(app_user=self.request.user)

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'pages/album_detail.html', context)

class AllPostView(ListView):
    model = Post
    template_name = 'pages/allposts.html'

    def get_queryset(self):
        return Post.objects.filter(app_user=self.request.user)


        # def user_photos(self, request):
    #     print('HELLO is this running?!?!')
    #     user_photos = Post.objects.get(app_user=request.user)
    #     context = {
    #         'photos': user_photos,
    #     }
    #     print(user_photos)
    #     return render(request, context, 'pages/dashboard.html')



# class AllPostView(ListView):
#     model = Post
#     template_name = 'pages/allposts.html'
#     context_object_name = 'posts'
#     # def get_queryset(self):
#     #     return Post.objects.filter(app_user=self.request.user)

#     def user_info(self, form):
#         form.instance.app_user = self.request.user
#         return super().user_info(form)

class PostView(ListView):
    model = Post
    template_name = 'pages/album.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Post.objects.filter(app_user=self.request.user)

class PostDetails(ListView):
    model = Post
    template_name = 'pages/postdetails.html'
    context_object_name = 'photos'
    print('HEY')
    def get_queryset(self):
        return Post.objects.filter(app_user=self.request.user)       
      
    # def user_photos(self, request):
    #     print('HELLO is this running?!?!')
    #     user_photos = Post.objects.get(app_user=request.user)
    #     context = {
    #         'photos': user_photos,
    #     }
    #     print(user_photos)
    #     return render(request, context, 'pages/dashboard.html')


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

    def get_form(self):
        if self.request.method == "POST":
            return PostForm(self.request.POST, request=self.request)
        else:
            return PostForm(request=self.request)

    def form_valid(self, form):
        form.instance.app_user = self.request.user
        return super().form_valid(form)
        
class CreatePostViewAlbum(CreateView): 
    model = Album
    form_class = PostForm
    template_name = 'pages/uploadpage.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Album.objects.filter(created_by=self.request.user)


class CreateAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'pages/albumpage.html'
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.app_user = self.request.user
        return super().form_valid(form)

# add method that saves user to the database
