from django.db import models
from django.core.validators import FileExtensionValidator
from django.shortcuts import reverse
from profiles.models import Profile

class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile_post", on_delete=models.CASCADE)
    caption = models.TextField(max_length=200, blank=True)
    images = models.ImageField(upload_to='post', blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    post_likes = models.ManyToManyField(Profile, related_name='post_like', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.profile} -- {self.caption[0:20]}"

    def get_like_url(self, *args, **kwargs):
        return reverse('post:post-likes', kwargs={'id': self.pk})

    def likes_no(self):
        return self.post_likes.count()
        
    def get_absolute_url(self):
        return reverse('post:post-detail', kwargs={"id": self.pk})
    
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.profile} commented {self.post} -- {self.comment[0:20]}"

class Feed(models.Model):
    profile = models.ManyToManyField(Profile, related_name='profile_feed')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_feed')
