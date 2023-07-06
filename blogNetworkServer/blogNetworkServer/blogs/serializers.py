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


class _AuthorsSerializer(serializers.Serializer):
    id_blog = serializers.CharField()
    id_user = serializers.CharField(max_length=100)


class _BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created_at = serializers.CharField()
    updated_at = serializers.CharField()
    owner = serializers.CharField()