from django.urls import path

from .views import CreatePostAPIView, PublishPostAPIView, LikePostAPIView, \
    ViewPostAPIView, CreateCommentApiView, GetPostsByUsernameApiView, \
    FindPostsByTitleApiView, FindPostsByTagsApiView, SortPostsByTitleAPIView,\
    SortPostsByTimeAPIView, ReverceSortPostsByTimeAPIView, ReverceSortPostsByTitleAPIView

urlpatterns = [
    path('create', CreatePostAPIView.as_view()),
    path('publish/<int:post>', PublishPostAPIView.as_view()),
    path('like/<int:post>', LikePostAPIView.as_view()),
    path('view/<int:post>', ViewPostAPIView.as_view()),
    path('createComment', CreateCommentApiView.as_view()),
    path('findByAuthor/<str:username>', GetPostsByUsernameApiView.as_view()),
    path('findByTitle/<str:query>', FindPostsByTitleApiView.as_view()),
    path('findByTags/<str:query>', FindPostsByTagsApiView.as_view()),
    path('sortByTitle', SortPostsByTitleAPIView.as_view()),
    path('reverceSortByTitle', ReverceSortPostsByTitleAPIView.as_view()),
    path('sortByTime', SortPostsByTimeAPIView.as_view()),
    path('reverceSortByTime', ReverceSortPostsByTimeAPIView.as_view()),
]