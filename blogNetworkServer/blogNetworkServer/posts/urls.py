from django.urls import path

from .views import CreatePostAPIView, PublishPostAPIView

urlpatterns = [
    path('create', CreatePostAPIView.as_view()),
    path('publish/<int:post>', PublishPostAPIView.as_view()),
]