from django.shortcuts import render,  get_object_or_404, HttpResponseRedirect
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
    
# view to show full post content + comments + likes


def single_post(request, post):
    all_posts = Post.objects.all().filter(status=1)
    post = get_object_or_404(Post, slug=post, )
    comments = post.comments.filter(accepted=True).order_by('created_on')
    clapped = False
    if post.claps.filter(id=request.user.id).exists():
        clapped = True
  
    # saving and showing comments by users/ displaying comment form
    new_comment = None
    if request.method == 'POST':
        comment_form = UserCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = UserCommentForm()
    return render(request, 'single_post.html', {'post': post,
                                                'comments': new_comment,
                                                'clapped': clapped,
                                                'commented': True,
                                                'comment_form': UserCommentForm(),
                                                'comments': comments,
                                                },)
                  