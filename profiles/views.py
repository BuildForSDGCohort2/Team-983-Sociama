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
                
        view_profile = self.get_object()
        my_profile = Profile.objects.get(pk=self.request.user.user_profile.pk)
        if view_profile in my_profile.followings.all():
            follow = True
        else:
            follow = False
        context['followed'] = follow
        return context

def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = PostForm(request.POST, request.FILES)   
        profile = Profile.objects.get(pk=request.user.user_profile.pk)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = profile
            instance.save()
            form = PostForm()

            return redirect(profile.get_absolute_url())

    context = {'form': form}
    return render(request, 'post/post_modal.html', context)

class ProfileList(generic.ListView):
    model = Profile
    template_name = 'profile/profile_list.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

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

# def follow(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     followr, created = Follow.objects.get_or_create(follower=request.user.user_profile, following=profile)
#     return redirect(request.META.get('HTTP_REFERER')) # return to same page

def follow(request, pk):
    
    if request.method == "POST":
        # logged in profile
        profile_ = request.user.user_profile.pk
        my_profile = Profile.objects.get(pk=profile_)
        # other profiles
        pk = request.POST.get('prof_pk')
        profile = Profile.objects.get(pk=pk)

        if profile in my_profile.followings.all():
            my_profile.followings.remove(profile)
            profile.followers.remove(my_profile)
        
        else:
            my_profile.followings.add(profile)
            profile.followers.add(my_profile)
        
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
        


