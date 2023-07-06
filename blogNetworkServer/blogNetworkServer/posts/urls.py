from django.urls import path

from .views import CreatePostAPIView, PublishPostAPIView, LikePostAPIView, \
    ViewPostAPIView, CreateCommentApiView

urlpatterns = [
    path('create', CreatePostAPIView.as_view()),
    path('publish/<int:post>', PublishPostAPIView.as_view()),
    path('like/<int:post>', LikePostAPIView.as_view()),
    path('view/<int:post>', ViewPostAPIView.as_view()),
    path('create-comment', CreateCommentApiView.as_view())
]