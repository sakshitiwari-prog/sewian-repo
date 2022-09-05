from django.contrib import admin
from django.urls import path,include
from sew import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('tailor',views.tailor,name='tailor')
] 
