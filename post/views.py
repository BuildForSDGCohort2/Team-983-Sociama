from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.views import generic
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from profiles.models import Profile

def posts(request):
    if request.user.is_authenticated:
        following = request.user.user_profile.get_following
        profile = request.user.user_profile
        posts = Post.objects.all().exclude(profile=profile)
        
        followings_post = Post.objects.filter(profile=following)
        
        follow_post = Post.objects.filter(profile=request.user.user_profile)
    
        context = {
            'posts': posts,
            'following': following,
            'follow_post': follow_post,

            'followings_post': followings_post,
        }
        return render(request, 'post/posts.html', context)
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('post:posts')
            else:
                messages.info(request, 'email or Password incorrect')
        return render(request, 'post/posts.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    is_liked = False
    if request.user.user_profile in post.post_likes.all():
        is_liked = True
    context = {
        'post': post,
        'comments': comments,
        'is_liked': is_liked,
        'likes_no': post.likes_no(),
    }
    return render(request, 'post/post_detail.html', context)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if request.user.user_profile in post.post_likes.all():
        post.post_likes.remove(request.user.user_profile)
        is_liked = False
    else:
        post.post_likes.add(request.user.user_profile)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
    # return redirect('/')