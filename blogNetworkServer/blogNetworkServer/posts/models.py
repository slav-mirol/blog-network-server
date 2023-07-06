from django.db import models
from ..users.models import User


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    is_published = models.CharField(default=False)
    created_at = models.DateTimeField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField()
    id_post = models.ForeignKey(to=Post, on_delete=models.CASCADE, default=0)


class Tag(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()


class PostTag(models.Model):
    id_tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE, related_name='tag2post')
    id_post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post2tag')
