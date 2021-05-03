from django.contrib import admin
from django.urls import path,include
from shop import views

urlpatterns = [
    path('', views.index,name="shop"),
    path('login', views.loginuser,name="login"),
    path('logout', views.logoutuser,name="logout"),
]
