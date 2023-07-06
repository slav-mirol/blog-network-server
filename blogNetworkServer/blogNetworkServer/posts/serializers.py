from rest_framework import serializers
from .models import Post, PostTag


class PostSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Post
        fields = ('author', 'title', 'body', 'id_blog')


class PostTagSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = PostTag
        fields = ('id_tag', 'id_post')
