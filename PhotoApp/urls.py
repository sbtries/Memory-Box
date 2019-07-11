from django.urls import path 

from .views import CreatePostView, DashboardView, CreateAlbumView, PostView, PostDetails, CreatePostViewAlbum

urlpatterns = [
    path('upload/', CreatePostView.as_view(), name='uploadpage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('albumpage/', CreateAlbumView.as_view(), name='createalbum'),
    path('album/', PostView.as_view(), name='posts'),
    path('postdetails/', PostDetails.as_view(), name='postdetails'),
    path('upload/', CreatePostViewAlbum.as_view(), name='uploadpagealbum'),
    # path('user_photos/<slug:user>', views.user_photos, name='user_photos'),
]