from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Post
        fields = [
            'caption',
            'images',
        ]
       
class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Add comment...', 'rows':4}))

    class Meta:
        model = Comment
        fields = [
            'comment',
        ]