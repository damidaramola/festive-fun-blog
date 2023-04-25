from django.shortcuts import render,  get_object_or_404
from .models import Post
from django.views import generic 
from .forms import UserCommentForm


# Create your views here.


# home page listing all posts 

def home_list(request):
    # query to select all posts from the posts table in database
    all_posts = Post.objects.all().filter(status=1)
    return render(request, 'index.html', {'posts': all_posts})
    paginate_by = 4
    
# view to show full post content


def single_post(request, post):
    all_posts = Post.objects.all().filter(status=1)
    post = get_object_or_404(Post, slug=post, )
    comments = post.comments.filter(accepted=True).order_by('created_on')
    clapped = False
    if post.claps.filter(id=request.user.id).exists():
        clapped = True
    return render(request, 'single_post.html', {
        'post': post,
        'comments': comments,
        'clapped': clapped,
        'comment_form': UserCommentForm(),
        },
                  )
    
    

