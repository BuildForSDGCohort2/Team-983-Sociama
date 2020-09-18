from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.views import generic
from .models import Post, Comment
from profiles.models import Profile

def posts(request):
    profile = request.user.user_profile
    posts = Post.objects.all().exclude(profile=profile)

    context = {
        'posts': posts,
    }
    return render(request, 'post/posts.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    is_liked = False
    # if post.post_likes.filter(profile=request.user.user_profile.first_name).exists():
    #     is_liked = True
    #     exist = 'yes Exsits'

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
    # if post.post_likes.filter(profile=request.user.user_profile.first_name).exists():
    #     post.post_likes.remove(request.user.user_profile)
    #     is_liked = False
    # else:
    #     post.post_likes.add(request.user.user_profile)
    #     is_liked = True

    if request.user.user_profile in post.post_likes.all():
        post.post_likes.remove(request.user.user_profile)
        is_liked = False
    else:
        post.post_likes.add(request.user.user_profile)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
    # return redirect('/')