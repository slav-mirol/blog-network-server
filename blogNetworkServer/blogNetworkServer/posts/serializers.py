from rest_framework import serializers
from .models import Post, PostTag, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Post
        fields = ('author', 'title', 'body', 'id_blog')


class PostTagSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = PostTag
        fields = ('id_tag', 'id_post')


class CommentSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Comment
        fields = ('author', 'body', 'created_at', 'id_post')


class _PostSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField(max_length=100)
    body = serializers.CharField()
    created_at = serializers.CharField()
    views = serializers.CharField()
    likes = serializers.CharField()

class _CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.CharField()
    id_post = serializers.CharField()

class _TagSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
