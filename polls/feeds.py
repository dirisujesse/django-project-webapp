from django.contrib.syndication.views import Feed

from .models import Question

class PollsFeed(Feed):
    title_template = 'Polls Feed'
    link = '/polls/'
    description_template = 'Latest Polls Feeds'
    
    def items(self):
        return Question.objects.all()
        
    def item_title(self, item):
        return item.question_text

    def item_description(self, item):
        return item.question_text
