from django.urls import path
from .views import CreateBlogAPIView

urlpatterns = [
    path('create', CreateBlogAPIView.as_view())
]