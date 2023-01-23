"""SocialProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from socialapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/register',views.SignUpView.as_view(),name="register"),
    path('',views.LoginView.as_view(),name="signin"),
    path('social/post/add',views.HomeView.as_view(),name="add-post"),
    path('social/allposts',views.PostList.as_view(),name="home"),
    path('social/post/<int:id>/comment/add',views.add_comment,name="add-comment"),
    path('social/posts/comment/<int:id>/likes',views.add_commentlikes,name="add-cmtlikes"),
    path('social/myposts',views.MyPosts.as_view(),name="myposts"),
    path('social/myprofile/add',views.MyProfile.as_view(),name="myprofile"),
    path('social/logout',views.sign_out,name="signout"),
    path('social/posts/<int:id>/likes',views.post_likes,name="add-likes"),
    path('social/myposts/<int:id>/delete',views.post_delete,name="post-delete"),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
