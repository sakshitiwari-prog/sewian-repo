from django.contrib import admin
from django.urls import path,include
from sew import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('account',views.account,name='account'),
    path('login',views.login,name='login')
] 
