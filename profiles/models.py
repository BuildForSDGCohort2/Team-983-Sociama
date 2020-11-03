from django.db import models
from users.models import User
from django.shortcuts import reverse, get_object_or_404

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
GENDER = (
    ('Male', 'Male'), 
    ('Female', 'Female'), 
    ('Others', 'Others'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    username = models.CharField(max_length=20, primary_key=True, blank=True)
    first_name = models.CharField(max_length=20, blank=True)    
    last_name = models.CharField(max_length=20, blank=True)
    age = models.DateField(blank=True, null=True)
    Hobbies = models.CharField(max_length=200, blank=True)
    work = models.CharField(max_length=200, blank=True)
    education = models.CharField(blank=True, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=7, blank=True)
    relationship = models.CharField(choices=RELATIONSHIP, max_length=23, blank=True)
    followers= models.ManyToManyField("Profile", blank=True, related_name='followerss') # people following profile
    followings = models.ManyToManyField("Profile", blank=True, related_name='followingss') # people profile is following 
    about = models.TextField(default='No Bio', blank=True)
    phone = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to='user/cover', default='user/happy.jpg', blank=True)
    picture = models.ImageField(upload_to='user', default='user/User.jpg', blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ('first_name', )
    
    def get_absolute_url(self):
        return reverse('profiles:profile', kwargs={"pk": self.pk})

    def get_follower(self):
        return self.followers.all()

    def get_follower_no(self):
        return self.followers.count()

    def get_following(self):
        return self.followings.all()

    def get_followering_no(self):
        return self.followings.count()
    
class Follow(models.Model):
    follower = models.ForeignKey(Profile, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} followed {self.following} on {self.created_at}"

    def save(self, **kwargs):
        if self.follower == self.following:
            raise ValueError("Cannot follow yourself.")
        super(Follow, self).save(**kwargs)


