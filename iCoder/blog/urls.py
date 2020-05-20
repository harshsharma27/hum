from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.blogHome,name='blogHome'),
    path('abou',views.abou,name='abou'),
    path('<str:slug>', views.blogPost,name='blogPost')
]