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

#class PostComment(models.Model):
#    id_post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='user2blog')
#    id_comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name='blog2user')
