from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from .forms import CommentForm
from django.contrib.auth import authenticate, login, logout
from profiles.models import Profile
from .models import Post, Comment, Message

def posts(request):
    if request.user.is_authenticated:
        profile = request.user.user_profile
        # posts = Post.objects.all().exclude(profile=profile)  

        profile_pk = request.user.user_profile.pk
        profiles = Profile.objects.get(pk=profile_pk)
        following = [prof for prof in profiles.followings.all()]

        posts = []
        qs = None
        # following posts
        for p in following:
            profile = p
            p_post = profile.profile_post.all()
            posts.append(p_post)
        my_post = request.user.user_profile.profile_post.all()
        posts.append(my_post)
        # sort and chain post query
        if len(posts)>0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created_at)

        paginator = Paginator(qs, 20)
        page_num = request.GET.get('page')
        post = paginator.get_page(page_num)
        
        context = {
            'posts': post,
            'following': following,
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

    c_form = CommentForm()
    if request.method == 'POST':
        c_form = CommentForm(request.POST)   
        profile = Profile.objects.get(pk=request.user.user_profile.pk)

        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.profile = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'is_liked': is_liked,
        'likes_no': post.likes_no(),
        'c_form': c_form,
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
    return redirect(request.META.get('HTTP_REFERER'))

