from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post

class PollsFeed(Feed):
    title_template = 'Posts Feed'
    link = '/'
    description_template = 'Latest Posts Feeds'
    
    def items(self):
        return Post.objects.all()
        
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
