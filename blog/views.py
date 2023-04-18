from django.shortcuts import render
from .models import Post

# Create your views here.


# home page listing all posts 

def home_list(request):
    # query to select all posts from the posts table in database
    all_posts = Post.objects.all().filter(status=1)
    return render(request, 'index.html', {'posts': all_posts})
    paginate_by = 4