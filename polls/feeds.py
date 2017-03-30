from django.contrib.syndication.views import Feed

from .models import Question

class PollsFeed(Feed):
    title = 'Polls Feed'
    link = '/polls/'
    description = 'Latest Polls Feeds'
    
    def items(self):
        return Question.objects.all()
        
    def item_title(self, item):
        return item.question_text

    def item_description(self, item):
        return item.question_text
