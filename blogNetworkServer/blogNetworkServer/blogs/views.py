from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogSerializer
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            res = {"error": "not found user {}".format(blog['owner'])}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


