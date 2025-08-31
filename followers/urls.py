from django.urls import path
from .views import FollowListCreateView

urlpatterns = [
    path('', FollowListCreateView.as_view(), name='follower-list-create'),
]