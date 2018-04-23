"""Netfilm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from application import views as app
# from djangoChat import views as chat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app.index),
	path('login/',app.login), #new 24.15.43
    path('loginpage/',app.login),
	path('register/',app.register),
    path('registerpage/',app.registerpage),
    path('delete/',app.delete),
    path('search/',app.search_movie),
    # path('search/',app.get_movie_comment),  #!!
    path('searchpage/',app.searchpage),
    path('chat/', app.chat),
    path('movieinfo/', app.movieinfo),
    path('makecomment/', app.make_comment),
    path('getmoviecomment/', app.get_movie_comment),
    path('userprofile/', app.userprofile),
    path('searchuser/', app.search_user)

    # change_pw
    # path('chat/',chat.urls),
    # url(r'^$', views.index, name='index'),
    # url(r'^login/$',views.login,name='login'),
    # url(r'^logout/$',views.logout,name='logout'),
    # url(r'^api/$',views.chat_api,name='chat_api'),
    # url(r'^api/users/$',views.logged_chat_users,name='logged_chat_users'),
    # url(r'^api/users/update/$',views.update_time,name='update_time'),
    # url(r'^chat/', include('djangoChat.urls')),
]
