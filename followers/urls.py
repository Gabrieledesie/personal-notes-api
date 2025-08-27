from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/', follow_user, name='follow'),
    path('unfollow/', unfollow_user, name='unfollow'),
]
