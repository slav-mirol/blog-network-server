from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, PostTagSerializer, _PostSerializer
from ..users.models import User
from .models import Post
from ..blogs.models import Blog, Authors


class CreatePostAPIView(APIView):

    def post(self, request):
        post = request.data
        try:
            is_author = Authors.objects.get(id_blog=post['id_blog'], id_user=post['author'])
            data = {
                "author": post['author'],
                "title": post['title'],
                "body": post['body'],
                "id_blog": post['id_blog'],
            }
            serializer = PostSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            for i in post['tag']:
                print(str(i), Post.objects.last().id)
                _serializer = PostTagSerializer(data={
                    'id_tag': str(i),
                    'id_post': Post.objects.last().id,
                })
                _serializer.is_valid(raise_exception=True)
                _serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            res = {"error": "user " + str(post["author"]) + " isn't author of blog {}".format(post['id_blog'])}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class PublishPostAPIView(APIView):
    def post(self, request, post):
        cur_post = Post.objects.get(id=post)
        cur_post.is_published = True
        cur_post.created_at = timezone.now()
        cur_post.save()
        blog = Blog.objects.get(id=cur_post.id_blog.id)
        blog.updated_at = timezone.now()
        blog.save()
        _serializer = _PostSerializer(instance=cur_post)
        return Response(_serializer.data, status=status.HTTP_202_ACCEPTED)


class LikePostAPIView(APIView):
    def post(self, request, post):
        cur_post = Post.objects.get(id=post)
        cur_post.likes += 1
        cur_post.save()
        _serializer = _PostSerializer(instance=cur_post)
        return Response(_serializer.data, status=status.HTTP_202_ACCEPTED)


class ViewPostAPIView(APIView):
    def post(self, request, post):
        cur_post = Post.objects.get(id=post)
        cur_post.views += 1
        cur_post.save()
        _serializer = _PostSerializer(instance=cur_post)
        return Response(_serializer.data, status=status.HTTP_202_ACCEPTED)