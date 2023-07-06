from django.urls import path
from .views import CreateBlogAPIView, AddAuthorToBlog, SubscribeToBlogApiView

urlpatterns = [
    path('create', CreateBlogAPIView.as_view()),
    path('add-author/<int:owner>/<int:blog>/<int:user>', AddAuthorToBlog.as_view()),
    path('subscribe/<int:blog>/<int:user>', SubscribeToBlogApiView.as_view()),
]