from django.shortcuts import render,  get_object_or_404, reverse, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import UserCommentForm


# Create your views here.


# home page listing all posts

def home_list(request):
    # query to select all posts from the posts table in database
    all_posts = Post.objects.all().filter(status=1)
    return render(request, 'index.html', {'posts': all_posts})
    paginate_by = 3

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
    @method_decorator(login_required)
    def post(self, request, post, *args, **kwargs):
        all_posts = Post.objects.all().filter(status=1)
        post = get_object_or_404(Post, slug=post)
        comments = post.comments.filter(accepted=True).order_by('created_on')
        clapped = False
        if post.claps.filter(id=self.request.user.id).exists():
            clapped = True

        comment_form = UserCommentForm(data=request.POST)
        if comment_form.is_valid():
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
    @login_required
    def post(self, request, post, *args, **kwargs):
        post = get_object_or_404(Post, slug=post)
        if post.claps.filter(id=request.user.id).exists():
            post.claps.remove(request.user)
        else:
            post.claps.add(request.user)
        return HttpResponseRedirect(reverse('blog:single_post',
                                            args=[post.slug]))


@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    if request.method == 'POST':
        comment_form = UserCommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            # Redirect to the single post view after successfully saving the edited comment
            return redirect('blog:single_post', post=comment.post.slug)

    else:
        comment_form = UserCommentForm(instance=comment)

    return render(request, "edit_comment.html", {"comment_form": comment_form})


@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    post_slug = comment.post.slug  # Get the slug of the post associated with the comment
    comment.delete()
    return redirect(reverse('blog:single_post', args=[post_slug]))


# list of cloudinary images
cloudinary_image_urls = [
    "https://res.cloudinary.com/dkkkwd8ho/image/upload/v1692427565/colour_festival_fxyjsz.jpg",
    "https://res.cloudinary.com/dkkkwd8ho/image/upload/v1692427565/friends-festival_orgdpa.jpg",
    "https://res.cloudinary.com/dkkkwd8ho/image/upload/v1692431149/cultural-festival-3_s166d1.jpg",
]

# Fetch all posts
posts = Post.objects.all()

# Update the featured_image field for each post using the corresponding image URL
for post, featured_image in zip(posts, cloudinary_image_urls):
    post.featured_image = featured_image
    post.save()
