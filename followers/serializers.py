from rest_framework import serializers
from .models import Follow
from users.models import User

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['follower', 'following', 'created_at']