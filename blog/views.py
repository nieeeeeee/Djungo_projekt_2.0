from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import detail, ListView

import blog
from blog.models import Post


# Create your views here.
# def post_list(request):
#     posts = Post.published.all()  # .filter(status='published')
#     return render(request, "blog/post/list.html", {"posts": posts})
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/post/detal.html', {"post": post})
