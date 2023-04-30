from django.shortcuts import render,  get_object_or_404, reverse 
from .models import Post
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import UserCommentForm


# Create your views here.


# home page listing all posts 

def home_list(request):
    # query to select all posts from the posts table in database
    all_posts = Post.objects.all().filter(status=1)
    return render(request, 'index.html', {'posts': all_posts})
    paginate_by = 4
    
# about page


def about(request):
    return render(request, 'about.html')

# view to show full post content + comments + likes


class SinglePost(View):
    def get(self, request, post, id=0, *args, **kwargs, ):
        all_posts = Post.objects.all().filter(status=1)
        post = get_object_or_404(Post, slug=post)
        comments = post.comments.filter(accepted=True).order_by('created_on')
        clapped = False
        if post.claps.filter(id=self.request.user.id).exists():
            clapped = True
           
        return render(
            request,
            "single_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "clapped": clapped,
                "comment_form": UserCommentForm()
            },
        )
    
    # saving and showing comments by users/ displaying comment form
    def post(self, request, post, *args, **kwargs):
        all_posts = Post.objects.all().filter(status=1)
        post = get_object_or_404(Post, slug=post)
        comments = post.comments.filter(accepted=True).order_by('created_on')
        clapped = False
        if post.claps.filter(id=self.request.user.id).exists():
            clapped = True
        
        comment_form = UserCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = UserCommentForm()
        
        return render(request,
                      "single_post.html", 
                      
                      {"post": post,
                       "comments": comments,
                       "clapped": clapped,
                       "commented": True,
                       "comment_form": comment_form, },)


    
        
# like(clap) and unlike(un-clap) posts


class ClapPosts(View):   
    def post(self, request, post, *args, **kwargs):
        post = get_object_or_404(Post, slug=post)
        if post.claps.filter(id=request.user.id).exists():
            post.claps.remove(request.user)
        else:
            post.claps.add(request.user)
        return HttpResponseRedirect(reverse('blog:single_post', args=[post.slug]))
    

