from django.urls import path
from .views import CreateBlogAPIView, AddAuthorToBlog, SubscribeToBlogApiView, FindBlogByTitleApiView, \
    FindBlogByAuthorsApiView, SortBlogsByTitleAPIView, ReverceSortBlogsByTitleAPIView, SortBlogsByTimeAPIView,\
    ReverceSortBlogsByTimeAPIView, DeleteBlog, UpdateBlog

urlpatterns = [
    path('create', CreateBlogAPIView.as_view()),
    path('add-author/<int:owner>/<int:blog>/<int:user>', AddAuthorToBlog.as_view()),
    path('subscribe/<int:blog>/<int:user>', SubscribeToBlogApiView.as_view()),
    path('findByTitle/<str:query>', FindBlogByTitleApiView.as_view()),
    path('findByAuthors/<str:query>', FindBlogByAuthorsApiView.as_view()),
    path('sortByTitle', SortBlogsByTitleAPIView.as_view()),
    path('reverceSortByTitle', ReverceSortBlogsByTitleAPIView.as_view()),
    path('sortByTime', SortBlogsByTimeAPIView.as_view()),
    path('reverceSortByTime', ReverceSortBlogsByTimeAPIView.as_view()),
    path('delete/<int:num>', DeleteBlog.as_view()),
    path('update', UpdateBlog.as_view())
]