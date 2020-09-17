from django.db import models
from django.core.validators import FileExtensionValidator
from django.shortcuts import reverse
from profiles.models import Profile

class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile_post", on_delete=models.CASCADE)
    caption = models.TextField(max_length=200, blank=True)
    images = models.ImageField(upload_to='post', blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.profile} -- {self.caption[0:20]}"

    def get_like_url(self, *args, **kwargs):
        return reverse('post:post-likes', kwargs={'id': self.pk})

    # def get_post(self):
    #     profile = self.profile
    #     return Profile.objects.filter(first_name=profile)

    class Meta:
        ordering = ('-created_at',)

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # LIKE_CHOICES = (('like', 'like'),('unlike', 'unlike'))
    # action = models.CharField(choices=LIKE_CHOICES, max_length=8)

    def __str__(self):
        return f"{self.profile} likes {self.post}"

class Unlike(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_unlike')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile} unlikes {self.post}"

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.profile} commented {self.post} -- {self.comment[0:20]}"


class Feed(models.Model):
    profile = models.ForeignKey(Profile, related_name='profile_feed', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_feed')