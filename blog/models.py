from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=80)
    content = models.TextField()
    date_pub = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:postdetail', kwargs={'pk': self.pk})

    def recently_published(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    recently_published.admin_order_field = 'date_pub'
    recently_published.boolean = True
    recently_published.short_description = 'Published recently?'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commentator = models.CharField(max_length=80, default='Anonymous')
    comment = models.TextField()
    comment_date_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return redirect ('blog:postdetail', kwargs={'pk': self.pk})

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.commentator