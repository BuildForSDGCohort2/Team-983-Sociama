from django.urls import path 
from . import views

app_name = 'post'
urlpatterns = [ 
    path('', views.posts, name='posts'),
    path('post/<int:id>', views.post_detail, name='post-detail'),
]