from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<pk>/', views.ProfileView.as_view(), name='profile'),
    path('update_profile/<pk>', views.updateprofile, name='update_profile'),
    path('friend_request/send/<pk>', views.send_friend_request, name='send_friend_request'),
    path('friend_request/cancel/<pk>', views.cancel_friend_request, name='cancel_friend_request'),
    path('friend_request/accept/<pk>', views.accept_friend_request, name='accept_friend_request'),
    path('friend_request/delete/<pk>', views.delete_friend_request, name='delete_friend_request'),


]
