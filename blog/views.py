from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic 


# Create your views here.


# home page listing all posts 

def home_list(request):
    # query to select all posts from the posts table in database
    all_posts = Post.objects.all().filter(status=1)
    return render(request, 'index.html', {'posts': all_posts})
    paginate_by = 4
    

def single_post(request, post):
    post = get_object_or_404(Post, slug=post, status=1)
    return render(request, 'single_post.html', {'post': post})

