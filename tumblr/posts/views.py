from django.shortcuts import render
from posts.models import Post
from markdown2 import Markdown

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('-time')
    return render(request, 'post.html', {"posts": posts})

def single_post(request, post_id):
    single_post = Post.objects.get(post_id=post_id)
    md = Markdown()
    single_post.content = md.convert(single_post.content)
    return render(request, 'single_post.html', {"post": single_post})