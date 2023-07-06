from django.urls import path
from .views import CreateBlogAPIView, AddAuthorToBlog

urlpatterns = [
    path('create', CreateBlogAPIView.as_view()),
    path('add-author/<int:blog>/<int:user>', AddAuthorToBlog.as_view())
]