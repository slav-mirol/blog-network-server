import datetime

from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, PostTagSerializer, _PostSerializer, CommentSerializer, \
    _TagSerializer, _CommentSerializer
from .models import Post, Tag, PostTag, Comment
from ..blogs.models import Blog, Authors
from ..users.models import User


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
    def put(self, request, post):
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
    def put(self, request, post):
        cur_post = Post.objects.get(id=post)
        cur_post.likes += 1
        cur_post.save()
        _serializer = _PostSerializer(instance=cur_post)
        return Response(_serializer.data, status=status.HTTP_202_ACCEPTED)


class ViewPostAPIView(APIView):
    def put(self, request, post):
        cur_post = Post.objects.get(id=post)
        cur_post.views += 1
        cur_post.save()
        _serializer = _PostSerializer(instance=cur_post)
        return Response(_serializer.data, status=status.HTTP_202_ACCEPTED)


class CreateCommentApiView(APIView):
    def post(self, request):
        comment = request.data
        data = {
            "author": comment['author'],
            "body": comment['body'],
            "created_at": timezone.now(),
            "id_post": comment['id_post'],
        }
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetLastPostsApiView(APIView):
    def get(self, request, num=5):
        posts = Post.objects.filter(is_published=True).order_by('created_at')[::-1]
        if num >= len(posts):
            serializer = _PostSerializer(instance=posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = _PostSerializer(instance=posts[:num], many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetLastPostsOfBlogApiView(APIView):
    def get(self, request, blog, num=5):
        posts = Post.objects.filter(is_published=True, id_blog=blog).order_by('created_at')[::-1]
        if num >= len(posts):
            serializer = _PostSerializer(instance=posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = _PostSerializer(instance=posts[:num], many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetPostsOfUserApiView(APIView):
    def get(self, request, user):
        posts = Post.objects.filter(is_published=True, author=user).order_by('created_at')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetPostsByUsernameApiView(APIView):
    def get(self, request, username):
        user = User.objects.filter(username__icontains=username)
        ids = []
        for i in user:
            ids.append(i.id)
        posts = Post.objects.filter(is_published=True, author__in=ids).order_by('created_at')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FindPostsByTitleApiView(APIView):
    def get(self, request, query):
        posts = Post.objects.filter(title__icontains=query.lower(), is_published=True).order_by('created_at')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FindPostsByTagsApiView(APIView):
    def get(self, request, query):
        query = query.split('-')
        for i in range(len(query)):
            query[i] = query[i].lower()
            query[i] = query[i].replace(query[i][0], query[i][0].upper(), 1)
        tags = Tag.objects.filter(title__in=query)
        ids = []
        for i in tags:
            ids.append(i.id)
        postsTag = PostTag.objects.filter(id_tag__in=ids)
        ids = []
        for i in postsTag:
            ids.append(i.id_post.id)
        posts = Post.objects.filter(id__in=ids, is_published=True).order_by('created_at')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SortPostsByTitleAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('title')
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReverceSortPostsByTitleAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('title')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SortPostsByTimeAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('created_at')
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReverceSortPostsByTimeAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('created_at')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SortPostsByLikesAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('likes')[::-1]
        serializer = _PostSerializer(instance=posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SortPostsByDateAPIView(APIView):
    def get(self, request, data, otdo):
        data = data.split(':')
        dates = []
        for i in data:
            dates.append(datetime.datetime.strptime(i, '%Y-%m-%d'))
        if len(data) == 1:
            if otdo == 'from':
                posts = Post.objects.filter(created_at__gte=data[0]).order_by('created_at')[::-1]
                serializer = _PostSerializer(instance=posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif otdo == 'before':
                posts = Post.objects.filter(created_at__lte=data[0]).order_by('created_at')[::-1]
                serializer = _PostSerializer(instance=posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif len(data) == 2 and otdo == 'fb':
            posts = Post.objects.filter(created_at__gte=data[0]) & Post.objects.filter(created_at__lte=data[1])
            serializer = _PostSerializer(instance=posts.order_by('created_at')[::-1], many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePost(APIView):
    def post(self, request, num):
        post = Post.objects.get(id=num).delete()
        res = {
            'answer': "post " + str(num) + " has been deleted"
        }
        return Response(res, status=status.HTTP_200_OK)


class DeleteComment(APIView):
    def post(self, request, num):
        comment = Comment.objects.get(id=num).delete()
        res = {
            'answer': "comment " + str(num) + " has been deleted"
        }
        return Response(res, status=status.HTTP_200_OK)


class DeleteTag(APIView):
    def post(self, request, num):
        tag = Tag.objects.get(id=num).delete()
        res = {
            'answer': "tag " + str(num) + " has been deleted"
        }
        return Response(res, status=status.HTTP_200_OK)


class UpdateTag(APIView):
    def post(self, request):
        tag = request.data
        Tag.objects.filter(id=tag['id']).update(title=tag['title'], description=tag['description'])
        cur_tag = Tag.objects.get(id=tag['id'])
        serializer = _TagSerializer(instance=cur_tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateComment(APIView):
    def post(self, request):
        comment = request.data
        Comment.objects.filter(id=comment['id']).update(
            author=comment['author'],
            body=comment['body'],
            created_at=datetime.datetime.strptime(comment['created_at'], '%Y-%m-%d')
        )
        cur_comm = Comment.objects.get(id=comment['id'])
        serializer = _CommentSerializer(instance=cur_comm)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdatePost(APIView):
    def post(self, request):
        post = request.data
        Post.objects.filter(id=post['id']).update(
            title=post['title'],
            body=post['body'],
            is_published=post['is_published'],
            created_at=datetime.datetime.strptime(post['created_at'], '%Y-%m-%d'),
            likes=post['likes'],
            views=post['views'],
            author=post['author']
        )
        cur_post = Post.objects.get(id=post['id'])
        serializer = _PostSerializer(instance=cur_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
