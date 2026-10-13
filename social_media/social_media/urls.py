"""
URL configuration for social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from accounts.views import *
from posts.views import PostView
from comments.views import CommentView
from likes.views import *
from followers.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post',PostView,basename="post")
router.register('comment',CommentView,basename="comment")
router.register('like',LikeView,basename="like")
router.register('follower',FollowerView,basename="follower")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignUpView.as_view({"post":"create"})),
    path('delete/<int:pk>',SignUpView.as_view({"delete":"destroy"})),
    path('login/',LoginView.as_view({"post":"create"})),
    path('profile/',ProfileView.as_view({"get":"list","post":"update","patch":"update"})),
]+router.urls
