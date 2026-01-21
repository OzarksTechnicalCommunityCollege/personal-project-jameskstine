from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    # posts = objects.filter(status=Post.Status.PUBLISHED)
    return render(
          request,
        'gallery/post/post_list.html',
        {'posts': posts}
    )

def post_detail(request, id):
        post = get_object_or_404(
              Post,
              id=id,
              status=Post.Status.PUBLISHED
        )
        return render(request, 'gallery/post_detail.html', {'post': post})