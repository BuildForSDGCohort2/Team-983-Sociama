from django import forms
from .models import Profile, Follow
import datetime

GENDER = (
    ('Male', 'Male'), 
    ('Female', 'Female'), 
    ('Others', 'Others'),
)
RELATIONSHIP = (
    ('Single', 'Single'), 
    ('In a relatinship', 'In a relatinship'),
    ('Engaged', 'Engaged'),
    ('Married', 'Married'),
    ('It\'s complicated', 'It\'s complicated'),
    ('Divored', 'Divored'),
    ('Widowed', 'Widowed'),
    ('In an open relationship', 'In an open relationship'),
)
YEAR_CHOICES = [(r) for r in range(1984, datetime.date.today().year+1)]

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    age = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control'}, years=YEAR_CHOICES), required=False,)
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-radio'}), choices=GENDER,)    
    relationship = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-radio'}), choices=RELATIONSHIP,)    
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 30, 'class':'form-control'}), required=False)
    cover = forms.ImageField()
    picture = forms.ImageField()
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    phone = forms.NumberInput(attrs={'class':'form-control'})

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'age',
            'gender',
            'relationship',
            'about',
            'cover',
            'picture',
            'country',
            'phone',
        ]

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = [
            'follower',
            'following',
        ]