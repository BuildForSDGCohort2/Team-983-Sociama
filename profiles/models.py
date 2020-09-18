from django.db import models
from users.models import User
from django.shortcuts import reverse
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=20, primary_key=True, blank=True)    
    last_name = models.CharField(max_length=20, blank=True)
    age = models.DateField(blank=True, null=True)
    Hobbies = models.CharField(max_length=200, blank=True)
    work = models.CharField(max_length=200, blank=True)
    education = models.CharField(blank=True, max_length=40)
    GENDER = (('Male', 'Male'), ('Female', 'Female'),)
    gender = models.CharField(choices=GENDER, max_length=7, blank=True)
    relationship = models.CharField(choices=RELATIONSHIP, max_length=23, blank=True)
    friends = models.ManyToManyField("Profile", blank=True)
    about = models.TextField(default='No Bio', blank=True)
    phone = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='user/cover', default='user/happy.jpg', blank=True)
    picture = models.ImageField(upload_to='user', default='user/User.jpg', blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('profiles:profile', kwargs={"pk": self.pk})

    def get_follower(self):
        profile = self.first_name
        return Follow.objects.filter(follower=profile)

    def get_follower_no(self):
        profile = self.first_name
        follow = Follow.objects.filter(follower=profile)
        return follow.count()

    def get_followering_no(self):
        profile = self.first_name
        following = Follow.objects.filter(following=profile)
        return following.count()

    def get_following(self):
        profile = self.first_name
        return Follow.objects.filter(following=profile)
    
    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='followings', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} followed {self.following} on {self.created_at}"

class FriendReqest(models.Model):
    from_user = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} sent {self.to_user} on {self.created_at}"