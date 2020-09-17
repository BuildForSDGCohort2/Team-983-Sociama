from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
]
