from django.conf.urls import url

from .views import *

app_name = 'blog'

urlpatterns = [
    url(r"^$", index, name='home'),
    url(r"^blog/$", PostList.as_view(), name='postlist'),
    url(r"(?P<pk>\d+)/$", PostDetail.as_view(), name='postdetail'),
    url(r"^post/new/$", NewPost.as_view(), name="post_new"),
    url(r'^(?P<post_id>\d+)/comment/$', new_comment, name="post_comment"),
]
