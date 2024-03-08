from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import detail

import blog
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()  # .filter(status='published')
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", date__year=year, date__month=month, date__day=day)

    return render(request, blog/post/detail.html , {"post": post})
