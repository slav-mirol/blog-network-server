"""
URL configuration for blogNetworkServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .users.urls import urlpatterns as users_urls
from .blogs.urls import urlpatterns as blogs_urls
from .posts.urls import urlpatterns as posts_urls
from .posts.views import GetLastPostsApiView, GetLastPostsOfBlogApiView, GetPostsOfUserApiView
from .blogs.views import GetLastBlogsApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(users_urls)),
    path('blog/', include(blogs_urls)),
    path('post/', include(posts_urls)),
    path('lastNposts/<int:num>', GetLastPostsApiView.as_view()),
    path('lastNblogs/<int:num>', GetLastBlogsApiView.as_view()),
    path('lastNpostsOfBlog/<int:blog>/<int:num>', GetLastPostsOfBlogApiView.as_view()),
    path('myPosts/<int:user>', GetPostsOfUserApiView.as_view()),
]
