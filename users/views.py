from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib import messages
from .forms import CreateUserForm
from .models import User
# from post.models import Post

def registerview(request):
    if request.user.is_authenticated:
        return redirect('post:posts')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User Account has been Created for ' + user)
                return redirect('post:posts')
        context = {'form': form}
        return render(request, 'profile/user.html', context)

def loginview(request):
    if request.user.is_authenticated:
        return redirect('post:posts')
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

        context = {}
        return render(request, 'profile/login.html', context)

def logoutview(request):
    logout(request)
    return redirect('users:login')

