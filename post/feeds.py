from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class LatestPostsFeed(Feed):
    title = 'Post'
    link = 'post:posts'
    description = 'Post feeds'

    def items(self):
        return Post.caption.all()[:3]

    def item_title(self, item):
        return item.caption

    def item_description(self, item):
        return truncatewords(item.caption, 30)