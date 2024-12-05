from django.urls import path
from . import views

urlpatterns=[
    path('',views.cloud_tech_login),
    path('cloud_tech_logout',views.cloud_tech_logout),
    path('register',views.register),
    path('home',views.home),
  
]