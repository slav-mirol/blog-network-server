import jwt
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler

from ..settings import SECRET_KEY
from .models import User
from .serializers import UserSerializer


class CreateUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = User.objects.get(username=username, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, SECRET_KEY)
                user_details = {}
                user_info = {}
                user_details['token'] = token
                user_info['id'] = "%s" % user.id
                user_info['username'] = "%s" % user.username
                user_info['is_admin'] = "%s" % user.is_admin
                user_details['user_info'] = user_info
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'error': 'please provide a email and a password'
        }
        return Response(res)


class DeleteUser(APIView):
    def post(self, request, num):
        user = User.objects.get(id=num).delete()
        res = {
            'answer': "user " + str(num) + " has been deleted"
        }
        return Response(res, status=status.HTTP_200_OK)


class UpdateUser(APIView):
    def post(self, request):
        user = request.data
        User.objects.filter(id=user['id']).update(
            username=user['username'],
            is_superuser=user['is_superuser'],
            is_admin=user['is_admin'],
        )
        cur_user = User.objects.get(id=user['id'])
        user_info = {
            'id': "%s" % cur_user.id,
            'username': "%s" % cur_user.username,
            'is_admin': "%s" % cur_user.is_admin
        }
        return Response(user_info, status=status.HTTP_200_OK)