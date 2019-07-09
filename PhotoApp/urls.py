from django.urls import path 

from .views import CreatePostView, DashboardView

urlpatterns = [
    path('upload/', CreatePostView.as_view(), name='uploadpage'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path('user_photos/<slug:user>', views.user_photos, name='user_photos'),
]