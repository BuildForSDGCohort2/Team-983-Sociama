from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<pk>/', views.ProfileView.as_view(), name='profile'),
    path('', views.ProfileList.as_view(), name='profile-list'),
    path('update_profile/<pk>', views.updateprofile, name='update_profile'),
    path('follow/<pk>', views.follow, name='follow'),
    path('create-post', views.create_post, name='create_post'),

]
