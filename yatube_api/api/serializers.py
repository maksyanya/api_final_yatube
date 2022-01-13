from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.generics import get_object_or_404

from posts.models import Comment
from posts.models import Follow
from posts.models import Group
from posts.models import Post
from posts.models import User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(
            user=self.context['request'].user, following=user).exists()
        if user == self.context['request'].user:
            raise serializers.ValidationError(
                "Вы не можете подписаться сам на себя"
            )
        if follow is True:
            raise serializers.ValidationError(
                "Вы уже подписаны на пользователя"
            )
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('id', 'user')
