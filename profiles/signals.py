from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile, Follow

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username)
        # Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.user_profile.save()

@receiver(post_save, sender=Follow)
def add_to_followers(sender, instance, created, **kwargs):
    follower_ = instance.follower
    following_ = instance.following
    
    follower_.followings.add(following_)
    
    # following_.followers.add(follower_)

    follower_.save()
    following_.save()

@receiver(post_save, sender=Follow)
def add_to_followings(sender, instance, created, **kwargs):
    follower_ = instance.follower
    following_ = instance.following
    
    # follower_.followings.add(following_)
    
    following_.followers.add(follower_)

    follower_.save()
    following_.save()



