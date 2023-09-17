from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('carousel/',views.carousel,name="carousel"),
    path("signup/",views.signup,name="signup"),
    path('loginuser/', views.loginuser, name ='loginuser'),
    path('logoutuser/', views.logoutuser, name ='logoutuser'),
    path('accountcreate/',views.accountcreate,name='accountcreate'),
    path('blog/',views.blog,name="blog"),
    path('chat/<int:id1>/<int:id2>',views.chat,name="chat"),
    path('readmore/<int:id1>',views.readmore,name='readmore'),
    
]
