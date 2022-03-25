
from unicodedata import name
from django import views
from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.login_profile, name='profile'),
]