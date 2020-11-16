from django.db import models
from django.core.validators import FileExtensionValidator
from django.shortcuts import reverse
from profiles.models import Profile

class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile_post", on_delete=models.CASCADE)
    caption = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to='post', blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    post_likes = models.ManyToManyField(Profile, related_name='post_like', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.profile} -- {self.caption[0:20]}"

    def get_like_url(self, *args, **kwargs):
        return reverse('post:post-likes', kwargs={'id': self.pk})

    def likes_no(self):
        return self.post_likes.count()
    
    def comment_no(self):
        return self.post_comment.count()

    def liked(self):
        is_liked = True
        not_liked = False
        if self.post_likes.count() > 0:
            return is_liked
        else:
            return not_liked
        
    def get_absolute_url(self):
        return reverse('post:post-detail', kwargs={"id": self.pk})
    
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    comment = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.profile} commented {self.post} -- {self.comment[0:20]}"

class Message(models.Model):
    from_prof = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='from_profile')
    to_prof = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='to_profile')
    message = models.TextField()

    def __str__(self):
        return f"{self.from_prof} sent {self.message[0:20]} to {self.to_prof}"
    
