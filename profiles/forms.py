from django import forms

from .models import Profile


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'about',
            'cover',
            'picture',
            'country',
        ]