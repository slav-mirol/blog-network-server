from django.urls import path
from .views import CreateUserAPIView, authenticate_user, DeleteUser

urlpatterns = [
    path('create', CreateUserAPIView.as_view()),
    path('auth', authenticate_user),
    path('delete/<int:num>', DeleteUser.as_view()),
]