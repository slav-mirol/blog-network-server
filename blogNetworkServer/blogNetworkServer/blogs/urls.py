from django.urls import path
from .views import CreateBlogAPIView, AddAuthorToBlog, SubscribeToBlogApiView, FindBlogByTitleApiView, \
    FindBlogByAuthorsApiView

urlpatterns = [
    path('create', CreateBlogAPIView.as_view()),
    path('add-author/<int:owner>/<int:blog>/<int:user>', AddAuthorToBlog.as_view()),
    path('subscribe/<int:blog>/<int:user>', SubscribeToBlogApiView.as_view()),
    path('findByTitle/<str:query>', FindBlogByTitleApiView.as_view()),
    path('findByAuthors/<str:query>', FindBlogByAuthorsApiView.as_view()),
]