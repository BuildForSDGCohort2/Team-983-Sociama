from django import forms
from .models import Profile, Follow

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'gender',
            'relationship',
            'about',
            'cover',
            'picture',
            'country',
        ]

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = [
            'follower',
            'following',
        ]