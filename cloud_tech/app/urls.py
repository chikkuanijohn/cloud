from django.urls import path
from . import views

urlpatterns=[
    path('',views.cloud_tech_login),
    path('register',views.register),
    path('home',views.home),
    path('logout',views.logout),
]