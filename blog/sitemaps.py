from django.contrib.sitemaps import Sitemap
from django.utils import timezone

from .models import Post

class PostSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(date_pub<=timezone.now())

    def lastmod(self, obj):
        return obj.date_pub
