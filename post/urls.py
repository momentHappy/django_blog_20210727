# coding=utf-8

from django.urls import path, re_path
from . import views

urlpatterns = (
    path('', views.queryAll),
    re_path(r'^page/(\d+)$', views.queryAll),
    re_path(r'^post/(\d+)$', views.detail),
    re_path(r'^category/(\d+)$', views.queryPostByCid),
    re_path(r'^archive/(\d+)/(\d+)$', views.queryPostByCreated),
)
