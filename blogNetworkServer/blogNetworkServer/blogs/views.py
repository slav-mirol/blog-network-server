from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogSerializer, AuthorsSerializer
from .models import Blog
from ..users.models import User


class CreateBlogAPIView(APIView):

    def post(self, request):
        blog = request.data
        try:
            user = User.objects.get(id=blog['owner'])
            data = {
                'title': "%s" % blog["title"],
                'description': "%s" % blog["description"],
                # 'created_at': "%s" % timezone.now().strftime('%d/%m/%Y %H:%M:%S'),
                'created_at': "%s" % timezone.now(),
                'owner': "%s" % blog['owner']
            }
            serializer = BlogSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            id_blog = Blog.objects.last().id
            _serializer = AuthorsSerializer(data={
                'id_blog': id_blog,
                'id_user': blog['owner']
            })
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            res = {"error": "not found user {}".format(blog['owner'])}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class AddAuthorToBlog(APIView):
    def post(self, request, owner, blog, user):
        try:
            cur_user = User.objects.get(id=user)
            cur_owner = User.objects.get(id=owner)
            cur_blog = Blog.objects.get(id=blog)
            if owner == cur_blog.owner:
                _serializer = AuthorsSerializer(data={
                    'id_blog': blog,
                    'id_user': user
                })
                _serializer.is_valid(raise_exception=True)
                _serializer.save()
                return Response(_serializer.data, status=status.HTTP_201_CREATED)
            else:
                res = {"error": "user " + str(owner) + " isn't owner of blog " + str(blog)}
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {"error": "not found user " + str(user) + "/" + str(owner) + " or blog " + str(blog)}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


