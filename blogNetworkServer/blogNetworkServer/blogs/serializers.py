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
