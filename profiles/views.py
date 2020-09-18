from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import UpdateUserForm
from post.forms import PostForm, CommentForm
from .models import Profile, Follow, FriendReqest
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
        context['form'] = PostForm()
        context['comments'] = CommentForm()

        return context

def profile_view(request, pk):
    p = Profile.objects.filter(pk=pk).first()
    u = p.profile
    sent_friend_request = FriendReqest.objects.filter(from_user=p.profile)
    received_friend_request = FriendReqest.objects.filter(to_user=p.profile)

    friends_list = p.friends.all()

    button_status = 'none'
    if p not in request.user.user_profile.friends.all():
        button_status = 'not_friend'

        if len(FriendReqest.objects.filter(from_user=request.user.user_profile).filter(to_user=p.profile)) == 1:
            button_status = 'friend_request_sent'

    context = {
        'sent_friend_request': sent_friend_request,
        'received_friend_request': received_friend_request,
        'friends_list': friends_list,
        'button_status': button_status,
        'u': u,
    }
    return render(request, 'profile/profile.html', context)

    

def updateprofile(request, pk):
    # profile = Profile.objects.get(pk=pk)
    profile = get_object_or_404(Profile, pk=pk)
    form = UpdateUserForm(instance=profile)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'profile/prof.html', context)

def profile_list(request):
    profile = get_object_or_404(Profile, pk=request.user.user_profile.pk)
    profiles = Profile.objects.all().exclude(profile=profile)

    context = {
        'profiles': profiles
    }
    return render(request, 'profile/profile_list.html', context)

def send_friend_request(request, pk):
    if request.user.user_profile.is_authenticated():
        profile = get_object_or_404(Profile, pk=pk)
        frequest, created = FriendReqest.objects.get_or_create(
            from_user = request.user.user_profile,
            to_user = profile
        )
        return redirect('/')

def cancel_friend_request(request, pk):
    if request.user.user_profile.is_authenticated():
        profile = get_object_or_404(Profile, pk=pk)
        frequest = FriendReqest.objects.filter(
            from_user = request.user.user_profile,
            to_user = profile
        ).first()
        frequest.delete()
        return redirect('/')

def accept_friend_request(request, pk):
    from_user = get_object_or_404(Profile, pk=pk)   
    frequest = FriendReqest.objects.filter(from_user = from_user, to_user = request.user.user_profile).first()
    user_1 = frequest.to_user
    user_2 = from_user
    user1.profile.friends.add(user2.profile)
    user2.profile.friends.add(user2.profile)
    frequest.delete()
    return redirect('/')

def delete_friend_request(request, pk):
    from_user = get_object_or_404(Profile, pk=pk)   
    frequest = FriendReqest.objects.filter(from_user = from_user, to_user = request.user.user_profile).first()
    frequest.delete()
    return redirect('/')