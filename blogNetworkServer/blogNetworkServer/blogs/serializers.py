from rest_framework import serializers
from .models import Blog, Authors


class BlogSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Blog
        fields = ('title', 'description', 'created_at', 'owner')


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Authors
        fields = ('id_blog', 'id_user')


class _AuthorsSerializer:
    id_blog = serializers.CharField()
    id_user = serializers.CharField(max_length=100)
