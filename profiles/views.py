from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import UpdateUserForm, FollowForm
from post.forms import PostForm, CommentForm
from .models import Profile, Follow
from post.models import Post

class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profile/profile.html'
    context_object_name = 'prof'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_ = self.kwargs.get("pk")
        pk = get_object_or_404(Profile, pk=pk_)
        context['posts'] = Post.objects.filter(profile=pk)
        context['follow'] = Follow.objects.filter(follower=pk)
        context['post'] = PostForm()
        context['comments'] = CommentForm()
        context['follow'] = FollowForm()        
        return context

def updateprofile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    form = UpdateUserForm(instance=profile)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(profile.get_absolute_url())

    context = {'form': form}
    return render(request, 'profile/update.html', context)

def follow(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    followr, created = Follow.objects.get_or_create(follower=request.user.user_profile, following=profile)
    return HttpResponseRedirect('/')