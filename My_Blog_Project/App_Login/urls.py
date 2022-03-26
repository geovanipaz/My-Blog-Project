
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
    path('change_profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('change-profile-image/', views.add_pro_pic, name='add_pro_pic'),
]