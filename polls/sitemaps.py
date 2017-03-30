from django.contrib.sitemaps import Sitemap

from .models import Question

class PollSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    choices = Question.choice_set.all()

    def items(self):
        return Question.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
