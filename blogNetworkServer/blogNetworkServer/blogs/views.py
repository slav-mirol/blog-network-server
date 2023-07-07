from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogSerializer, AuthorsSerializer, _BlogSerializer, SubscriptionsSerializer
from .models import Blog, Subscriptions
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
            print(owner, cur_blog.owner)
            if owner == cur_blog.owner.id:
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


class GetLastBlogsApiView(APIView):
    def get(self, request, num=5):
        blogs = Blog.objects.order_by('updated_at')[::-1]
        if num >= len(blogs):
            serializer = _BlogSerializer(instance=blogs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = _BlogSerializer(instance=blogs[:num], many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeToBlogApiView(APIView):
    def post(self, request, blog, user):
        try:
            cur_user = User.objects.get(id=user)
            cur_blog = Blog.objects.get(id=blog)
            _serializer = SubscriptionsSerializer(data={
                'id_user': user,
                'subscribe_blog': blog
            })
            _serializer.is_valid(raise_exception=True)
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            res = {"error": "not found user " + str(user) + " or blog " + str(blog)}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class GetSubscibeOfUserApiView(APIView):
    def get(self, request, user):
        subscribes = Subscriptions.objects.filter(id_user=user)
        ids = []
        for i in subscribes:
            ids.append(i.subscribe_blog.id)
        blogs = Blog.objects.filter(id__in=ids).order_by('updated_at')[::-1]
        serializer = _BlogSerializer(instance=blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FindBlogByTitleApiView(APIView):
    def get(self, request, query):
        blogs = Blog.objects.filter(title__icontains=query.lower())
        serializer = _BlogSerializer(instance=blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
