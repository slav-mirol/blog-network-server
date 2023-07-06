from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Blog
        fields = ('title', 'description', 'created_at', 'owner')