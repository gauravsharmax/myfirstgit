from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('',views.home , name='HTML'),
    path('home', views.index, name = 'HOME'),
    path('contactus',views.contactus, name =  'contactus'),
    path('coffee',views.coffee,name= 'ice'),
    path('starter',views.starter, name = 'Starter')
]
