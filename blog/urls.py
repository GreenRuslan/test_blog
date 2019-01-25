# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('single/<int:pk>', views.post_single, name="blog_post"),
]