from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class PostFeed(Feed):
    title = 'Posts Feed'
    link = '/'
    description = 'Latest Posts Feeds'
    
    def items(self):
        return Post.objects.all()
        
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
