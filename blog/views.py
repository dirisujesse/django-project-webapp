from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from django.utils import timezone
from django.views import generic

from .models import Post, Comment

def index(request):
    return render(request, 'blog/home.html')

class PostList(generic.ListView):
    template_name = 'blog\list.html'
    context_object_name = 'postobject'

    def get_queryset(self):
        return Post.objects.filter(date_pub__lte=timezone.now()).order_by('-date_pub')[:5]

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog\details.html'

    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(date_pub__lte=timezone.now())

class NewPost(generic.CreateView):
    model = Post
    fields = ['title', 'author', 'content', 'date_pub']

# class CommentForm(generic.CreateView):
#     model = Comment
#     fields = ['post', 'commentator', 'comment']


def new_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:postdetail', post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})