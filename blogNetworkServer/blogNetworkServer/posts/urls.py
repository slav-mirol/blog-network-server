from django.urls import path

from .views import CreatePostAPIView

urlpatterns = [
    path('create', CreatePostAPIView.as_view()),
]