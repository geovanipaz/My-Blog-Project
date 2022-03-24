from django import views
from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list')
]