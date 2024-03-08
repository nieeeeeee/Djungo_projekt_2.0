from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all() #.filter(status='published')
    return render(request, "blog/post/list.html",{"posts":posts})