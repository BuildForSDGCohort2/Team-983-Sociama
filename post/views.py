from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Post, Like, Unlike
from profiles.models import Profile

def posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'post/posts.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)

# def like_unlike_post(request):
#     profile = request.user.user_profile
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post_obj = Like.objects.get(id=post_id)
#         profile = Profile.objects.get(profile=profile)

#         if profile in post_obj.post.filter(id=id).all():
#             post_obj.