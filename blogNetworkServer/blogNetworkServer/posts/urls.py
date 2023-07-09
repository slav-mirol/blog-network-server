from django.urls import path

from .views import CreatePostAPIView, PublishPostAPIView, LikePostAPIView, \
    ViewPostAPIView, CreateCommentApiView, GetPostsByUsernameApiView, \
    FindPostsByTitleApiView, FindPostsByTagsApiView, SortPostsByTitleAPIView, \
    SortPostsByTimeAPIView, ReverceSortPostsByTimeAPIView, ReverceSortPostsByTitleAPIView,\
    SortPostsByLikesAPIView, SortPostsByDateAPIView, DeletePost, DeleteTag, DeleteComment, \
    UpdateTag, UpdateComment, UpdatePost, RelevationSortPost

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
    path('sortByLikes', SortPostsByLikesAPIView.as_view()),
    path('sortByDate/<str:data>/<str:otdo>', SortPostsByDateAPIView.as_view()),
    path('deletePost/<int:num>', DeletePost.as_view()),
    path('deleteComment/<int:num>', DeleteComment.as_view()),
    path('deleteTag/<int:num>', DeleteTag.as_view()),
    path('updateTag', UpdateTag.as_view()),
    path('updateComment', UpdateComment.as_view()),
    path('update', UpdatePost.as_view()),
    path('relevationSort', RelevationSortPost.as_view()),
]