from django.db import models
from ..users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Authors(models.Model):
    id_blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE, related_name='user2blog')
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blog2user')
